## Giải thích từng hàm code 

**Thực hành 6 (4-Queens)**

### *import numpy as np*
- Thư viện numpy dùng để tạo và thao tác với mảng hai chiều (ma trận), giúp biểu diễn và in bàn cờ.

### *def is_valid_state(state, num_queens):*
- Kiểm tra trạng thái hiện tại có phải là lời giải hợp lệ không.
- Trả về True nếu số lượng quân hậu đã đặt đúng bằng số quân hậu cần thiết `num_queens`, tức là đã đặt đủ mỗi hàng một quân hậu.

### *def get_candidates(state, num_queens):*
- Trả về tập các cột có thể đặt quân hậu tiếp theo ở hàng hiện tại.
- Loại bỏ các cột đã bị tấn công bởi các quân hậu trước đó:
    - Cùng cột (vertical)
    - Cùng đường chéo chính và phụ (diagonal)
- Duyệt qua từng quân hậu đã đặt, loại bỏ các vị trí không hợp lệ khỏi tập ứng viên.

### *def search(state, solutions, num_queens):*
- Hàm đệ quy/backtracking để tìm tất cả lời giải.
- Nếu trạng thái hiện tại hợp lệ (đủ quân hậu), thêm vào danh sách lời giải.
- Nếu chưa đủ, thử đặt quân hậu vào từng cột hợp lệ tiếp theo (ứng viên), gọi đệ quy cho hàng tiếp theo.
- Sau khi thử xong thì loại bỏ quân hậu vừa đặt `backtrack` để thử các khả năng khác.

### *def solve(num_queens):*
- Là giải pháp cho đa số các bài 4-Queens
- Khởi tạo trạng thái rỗng và danh sách lời giải, sau đó gọi hàm search để tìm tất cả lời giải.
- Trả về danh sách các lời giải hợp lệ.

### *if __name__ == "__main__":*
- Là hàm quan trọng để có chạy được phương tình
- Chúng sẽ yêu cầu nhập số quân hậu (n) từ bàn phím.
- Gọi hàm `def solve()` để tìm ra được lời giải.
- Đưa ra kết quả tổng số lời giải tìm được.
- Với mỗi lời giải:
    - Tạo bàn cờ trắng (ma trận toàn dấu "-").
    - Đặt quân hậu lên bàn cờ theo lời giải (trong đây tượng trưng kí hiệu **Q**)
    - In bàn cờ và tọa độ các quân theo từng lời giải


## Giải thích từng hàm - Thực hành 7 (8-Queens)

### *import numpy as np, import random*
- Cũng như bài 4-Queens, nhưng lần này thêm thư viện `random` vào để hỗ trợ việc tạo ra số ngẫu nhiên

### *def is_valid_state(state, num_queens):*
- Hàm này kiểm tra xem trạng thái hiện tại có phải là một lời giải hợp lệ không.
- Trả về `True` nếu số lượng quân hậu đã đặt đúng bằng số quân hậu cần thiết `num_queens`, tức là đã đặt đủ mỗi hàng một quân hậu.

### *def get_candidates(state, num_queens):*
- Trả về tập các cột có thể đặt quân hậu tiếp theo ở hàng hiện tại.
- Các cột đã bị tấn công bởi các quân hậu trước đó sẽ được loại bỏ dần yêu cầu:
    - Cùng cột (vertical)
    - Cùng đường chéo chính và phụ (diagonal)
- Duyệt qua từng quân hậu đã đặt, loại bỏ các vị trí không hợp lệ ra khỏi bảng.

### *def search(state, solutions, num_queens):*
- Là thuật toán quay lui `backtracking`.
- Nếu trạng thái hiện tại hợp lệ (đủ quân hậu), thêm vào danh sách lời giải.
- Nếu chưa đủ, thử đặt quân hậu vào từng cột hợp lệ tiếp theo, gọi đệ quy cho hàng tiếp theo.
- Sau khi thử xong thì loại bỏ quân hậu vừa đặt `backtracking` để thử các khả năng khác.

### *def solve(num_queens):*
- Hàm tổng quát lại để giải bài toán **N-Queens**.
- Khởi tạo trạng thái rỗng và danh sách lời giải, sau đó gọi hàm search để tìm tất cả lời giải.
- Trả về danh sách các lời giải hợp lệ.

### *if __name__ == "__main__":*
- Là hầu như phần chạy chính phương trình.
- Yêu cầu nhập số quân hậu (n) từ bàn phím (thường là 8 cho bài toán 8-Queens).
- Gọi hàm `def solve()` để tìm lời giải.
- In ra tổng số lời giải tìm được.
- Với mỗi lời giải:
    - Tạo bàn cờ trắng (ma trận theo tương ứng toàn dấu "-").
    - Đặt quân hậu lên bàn cờ theo lời giải.
    - In bàn cờ ra màn hình để dễ hình dung.