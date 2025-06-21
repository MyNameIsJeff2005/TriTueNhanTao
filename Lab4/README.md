## Ghi chú kết quả và phân tích sự khác biệt giữa 5 bài tập

### **Bài tập 1 & 2: Tối ưu hàm một biến với GA**
- **Kết quả:** Khi chạy thuật toán di truyền cho hàm `h(x) = \sin(x) + \cos(x)`, nghiệm tìm được rất gần với nghiệm lý thuyết (`h(x) \approx 0.7854`, `h(x) \approx 1.4142`). Quá trình hội tụ diễn ra khá nhanh nếu chọn tham số hợp lý.
- **Phân tích:** Thuật toán di truyền rất phù hợp cho bài toán tối ưu một biến. Mình thấy quần thể ban đầu rất đa dạng, nhưng càng về sau thì các cá thể tốt dần chiếm ưu thế, dẫn đến nghiệm tối ưu gần đúng với giá trị thực tế.

### **Bài tập 3: Ảnh hưởng tham số GA**
- **Kết quả:** Khi mình thay đổi các tham số như kích thước quần thể, mutation_rate, crossover_rate, số thế hệ,... thì tốc độ hội tụ và chất lượng nghiệm thay đổi rõ rệt.
- **Phân tích:**  
    - Nếu tăng kích thước quần thể thì thuật toán tránh bị kẹt ở cực trị cục bộ, nhưng thời gian chạy lâu hơn.
    - Mutation_rate thấp quá thì dễ hội tụ sớm, còn cao quá thì nghiệm dao động, khó hội tụ.
    - Crossover_rate cao giúp phối hợp gen tốt, nhưng nếu quá cao thì lại phá vỡ cấu trúc tốt.
    - Số thế hệ lớn thì nghiệm tốt hơn, nhưng phải chờ lâu hơn.

### **Bài tập 4: So sánh các phương pháp lựa chọn**
- **Kết quả:**  
    - **Roulette Wheel:** Hội tụ nhanh, ưu tiên cá thể tốt nhưng dễ mất đa dạng.
    - **Tournament:** Hội tụ chậm hơn nhưng duy trì đa dạng tốt hơn, ít bị kẹt cực trị cục bộ.
    - **Random:** Hội tụ rất chậm, nghiệm thường kém hơn.
- **Phân tích:** Mình nhận thấy phương pháp lựa chọn ảnh hưởng rất lớn đến kết quả. Nếu muốn hội tụ nhanh thì dùng Roulette, còn muốn đa dạng thì dùng Tournament. Random thì chỉ nên dùng để tham khảo vì hiệu quả không cao.

### **Bài tập 5: Trực quan hóa quần thể**
- **Kết quả:**  
    - Lúc đầu, các cá thể phân bố rộng khắp không gian tìm kiếm.
    - Ở giữa quá trình, các cá thể dần hội tụ về vùng tối ưu, nhưng vẫn còn sự đa dạng nhất định.
    - Đến cuối, quần thể tập trung gần nghiệm tối ưu, đa dạng giảm mạnh.
- **Phân tích:**  
    - Việc trực quan hóa giúp mình dễ dàng quan sát quá trình hội tụ và mức độ đa dạng của quần thể.
    - Nếu thấy hội tụ quá nhanh, mình sẽ tăng mutation_rate để duy trì đa dạng.
    - Nếu hội tụ chậm, có thể giảm mutation_rate hoặc tăng số thế hệ để cải thiện kết quả.