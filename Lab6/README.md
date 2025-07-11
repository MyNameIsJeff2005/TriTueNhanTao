## Công nghệ sử dụng
- **PyTorch**: Framework mạnh mẽ cho học sâu, hỗ trợ GPU, dễ xây dựng mạng nơ-ron.
- **Torchvision**: Thư viện tải và xử lý dữ liệu ảnh (MNIST).
- **Matplotlib, NumPy**: Trực quan hóa kết quả, xử lý dữ liệu.

## Thuật toán sử dụng
- **Convolutional Neural Network (CNN)**: Mạng nơ-ron tích chập cho nhận diện ảnh số viết tay.
- **Loss Function**: CrossEntropyLoss (phù hợp phân loại nhiều lớp).
- **Optimizer**: SGD (Stochastic Gradient Descent) với momentum.

## Giải thích cách hoạt động
- **Tầng tích chập (Convolution)**: Tìm đặc trưng nhỏ trong ảnh (cạnh, góc).
- **Hàm kích hoạt (ReLU)**: Loại bỏ giá trị âm, giữ nét chính.
- **Pooling**: Giảm kích thước, giữ thông tin quan trọng.
- **Fully Connected**: Ghép đặc trưng, phân loại ảnh.
- **Huấn luyện**: Lặp qua nhiều epoch để tối ưu trọng số.
- **Learning rate**: Điều chỉnh tốc độ học của mô hình.

---

## Câu 1: Thay đổi số lượng epoch
**Code:** Tăng số epoch từ 5 lên 10 trong vòng lặp huấn luyện.
**Kết quả:** Loss giảm đều hơn, độ chính xác trên tập test thường tăng. Nếu epoch quá lớn có thể gây overfitting.
**Giải thích:** Epoch tăng giúp mô hình học lâu hơn, nhưng cần cân nhắc để tránh học thuộc dữ liệu huấn luyện.

---

## Câu 2: Thêm một tầng tích chập
**Code:** Thêm tầng tích chập thứ ba (`conv3`) vào mô hình, sửa lại tầng fully connected cho phù hợp.
**Kết quả:** Độ chính xác trên tập test thường tăng, mô hình học được đặc trưng phức tạp hơn.
**Giải thích:** Thêm tầng giúp mô hình mạnh hơn, nhưng nếu quá phức tạp mà dữ liệu không đủ lớn có thể gây overfitting.

---

## Câu 3: Thay đổi learning rate
**Code:** Thử với hai giá trị learning rate: 0.001 và 0.1.
**Kết quả:**  
- Learning rate nhỏ (0.001): mô hình học chậm, loss giảm từ từ, ổn định.
- Learning rate lớn (0.1): mô hình học nhanh nhưng loss dao động mạnh, có thể không hội tụ.
**Giải thích:** Learning rate ảnh hưởng trực tiếp đến tốc độ và độ ổn định của quá trình học.

---

## Câu 4: Vẽ thêm feature map từ tầng conv2
**Code:** Sửa hàm trực quan hóa để vẽ thêm hai feature map từ tầng conv2.
**Kết quả:** Feature map tầng 1 thể hiện nét cơ bản, tầng 2 thể hiện đặc trưng phức tạp hơn, hình ảnh trừu tượng hơn.
**Giải thích:** Các tầng sâu hơn trong CNN sẽ học đặc trưng tổng hợp từ các tầng trước, giúp mô hình nhận diện tốt hơn.