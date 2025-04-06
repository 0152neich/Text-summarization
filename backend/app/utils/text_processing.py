import re
import torch
import numpy as np
from underthesea import word_tokenize, sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from config.configs import vietnamese_stopwords, model_path

class TextProcessing:
    def __init__(self):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2").to(self.device)

    def clean_text(self, text: str) -> str:
        """ Clean text by removing special characters and extra whitespaces

        Args:
            text (str): input text

        Returns:
            str: cleaned text
        """
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.]', '', text)
        return text.strip()

    def process_sentences(self, text: str) -> str:
        """Tokenize text and remove stopwords

        Args:
            text (str): input text
        
        Returns:
            str: processed text
        """
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.isalnum() and word not in vietnamese_stopwords]
        return ' '.join(filtered_words)

    def build_similarity_matrix(self, sentences: list) -> np.ndarray:
        """ Build similarity matrix from sentences

        Args:
            sentences (list): list of sentences

        Returns:
            np.ndarray: similarity matrix
        """
        preprocessed_sentences = [self.process_sentences(sentence) for sentence in sentences]
        embeddings = self.model.encode(
            preprocessed_sentences,
            batch_size=32,
            convert_to_tensor=False,
            show_progress_bar=False
        )
        return cosine_similarity(embeddings)

    def textrank_summary(self, text: str, num_sentences: int = None) -> str:
        """Apply TextRank to summarize text

        Args:
            text (str): Preprocessed text (default from process_sentences)
            num_sentences (int): Number of sentences in summary
        Returns:
            str: Summary text
        """
        sentences = sent_tokenize(text)
        if num_sentences is None:
            num_sentences = max(1, len(sentences) // 2)
        if len(sentences) <= num_sentences:
            return ' '.join(sentences)

        similarity_matrix = self.build_similarity_matrix(sentences)
        graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(graph, max_iter=100, tol=1e-06)

        for i in range(len(sentences)):
            scores[i] = scores[i] + (1.0 / (i + 1)) * 0.5

        ranked_sentences = sorted(((scores[i], s, i) for i, s in enumerate(sentences)), reverse=True)
        selected_indices = sorted([i for _, _, i in ranked_sentences[:num_sentences]])
        summary = [sentences[i] for i in selected_indices]
        return ' '.join(summary)