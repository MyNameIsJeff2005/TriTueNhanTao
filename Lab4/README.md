## Ghi chú kết quả và phân tích sự khác biệt giữa 5 bài tập

### **Bài tập 1 & 2: Tối ưu hàm một biến với GA**
- **Kết quả:** Thuật toán di truyền tìm được nghiệm gần đúng với nghiệm lý thuyết của hàm $h(x) = \sin(x) + \cos(x)$, hội tụ về $x \approx 0.7854$ với $h(x) \approx 1.4142$.
- **Phân tích:** GA hoạt động tốt với bài toán một biến, hội tụ nhanh nếu tham số hợp lý. Đa dạng quần thể giảm dần qua các thế hệ, nghiệm tối ưu đạt được gần với giá trị thực tế.

### **Bài tập 3: Ảnh hưởng tham số GA**
- **Kết quả:** Khi thay đổi các tham số như kích thước quần thể, mutation_rate, crossover_rate, số thế hệ, tốc độ hội tụ và chất lượng nghiệm thay đổi rõ rệt.
- **Phân tích:**  
    - Quần thể lớn giúp tránh kẹt cực trị cục bộ nhưng tốn thời gian.
    - Mutation_rate quá thấp dễ hội tụ sớm, quá cao gây nhiễu loạn.
    - Crossover_rate cao giúp phối hợp gen tốt nhưng nếu quá cao có thể phá vỡ cấu trúc tốt.
    - Số thế hệ lớn giúp nghiệm tốt hơn nhưng tăng thời gian chạy.

### **Bài tập 4: So sánh các phương pháp lựa chọn**
- **Kết quả:**  
    - **Roulette Wheel:** Hội tụ nhanh, ưu tiên cá thể tốt nhưng dễ mất đa dạng.
    - **Tournament:** Hội tụ chậm hơn nhưng duy trì đa dạng tốt hơn, ít bị kẹt cực trị cục bộ.
    - **Random:** Hội tụ rất chậm, nghiệm thường kém hơn.
- **Phân tích:** Phương pháp lựa chọn ảnh hưởng lớn đến tốc độ hội tụ và chất lượng nghiệm. Nên chọn phương pháp phù hợp với bài toán và mục tiêu tối ưu.

### **Bài tập 5: Trực quan hóa quần thể**
- **Kết quả:**  
    - Đầu quá trình: Quần thể phân bố rộng khắp không gian tìm kiếm.
    - Giữa quá trình: Các cá thể dần hội tụ về vùng tối ưu, vẫn còn đa dạng.
    - Cuối quá trình: Quần thể tập trung gần nghiệm tối ưu, đa dạng giảm mạnh.
- **Phân tích:**  
    - Trực quan hóa giúp quan sát quá trình hội tụ và mức độ đa dạng của quần thể.
    - Nếu hội tụ quá nhanh, nên tăng mutation_rate để duy trì đa dạng.
    - Nếu hội tụ chậm, có thể giảm mutation_rate hoặc tăng số thế hệ.

---

**Tổng kết:**  
- Các bài tập cho thấy thuật toán di truyền rất linh hoạt, hiệu quả phụ thuộc mạnh vào tham số và phương pháp lựa chọn.
- Việc trực quan hóa và thử nghiệm tham số giúp hiểu sâu hơn về cơ chế hội tụ, tránh kẹt cực trị cục bộ và tối ưu hóa kết quả.