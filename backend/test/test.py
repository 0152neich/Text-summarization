from app.utils.text_processing import TextProcessing

if __name__ == "__main__":
    text = "Một buổi sáng trong mùa hạ, không khí mát lành, ánh nắng ban mai nhẹ nhàng len lỏi, tô điểm cho khung cảnh quê em. Trên cánh đồng rộng lớn, những bông lúa chín mừng mình, nhấp nhô theo làn gió nhẹ"
    text_processing = TextProcessing(text)
    text = text_processing.clean_text(text)
    text = text_processing.process_sentences(text)
    text_summary = text_processing.textrank_summary(text)
    print(text_summary)
