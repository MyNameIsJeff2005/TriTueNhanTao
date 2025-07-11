## Giải thích code từng câu
### **Câu 1: Thay đổi số lượng epoch**
**Giải thích:**  
Ở phần này, mình tăng số epoch từ 5 lên 10 trong vòng lặp huấn luyện. Việc này giúp mô hình có thêm thời gian để học từ dữ liệu, nên loss giảm đều hơn và độ chính xác trên tập test thường tăng lên. Tuy nhiên, nếu epoch quá lớn mà không điều chỉnh các tham số khác, mô hình có thể bị overfitting (học thuộc dữ liệu huấn luyện, kém tổng quát hóa).

### **Câu 2: Thêm một tầng tích chập**
**Giải thích:**  
Mình thêm một tầng tích chập thứ ba (`conv3`) vào mô hình. Sau mỗi tầng tích chập đều có ReLU và pooling. Việc thêm tầng này giúp mô hình học được các đặc trưng phức tạp hơn trong ảnh, từ đó có thể tăng độ chính xác. Tuy nhiên, nếu mô hình quá phức tạp mà dữ liệu không đủ lớn, có thể dẫn đến overfitting.

### **Câu 3: Thay đổi learning rate**
**Giải thích:**  
Ở câu này, mình thử hai giá trị learning rate khác nhau: 0.001 và 0.1.  
- Với learning rate nhỏ (0.001), mô hình học chậm, loss giảm từ từ nhưng ổn định, ít bị dao động.
- Với learning rate lớn (0.1), mô hình học rất nhanh nhưng loss có thể dao động mạnh, thậm chí không hội tụ nếu quá lớn.
Việc chọn learning rate phù hợp là rất quan trọng để mô hình học hiệu quả.

### **Câu 4: Vẽ thêm feature map từ tầng conv2**
**Giải thích:**  
Mình sửa hàm trực quan hóa để vẽ thêm hai feature map từ tầng tích chập thứ hai (`conv2`).  
- Feature map tầng 1 (conv1) thường thể hiện các nét cơ bản như cạnh, góc.
- Feature map tầng 2 (conv2) thể hiện các đặc trưng phức tạp hơn, là sự kết hợp của nhiều nét từ tầng trước, nên hình ảnh trừu tượng hơn.
Việc này giúp mình hiểu rõ hơn về cách CNN học và trích xuất đặc trưng qua từng