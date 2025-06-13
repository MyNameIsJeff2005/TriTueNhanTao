#  Thuật Toán Duyệt Đồ Thị (Graph Traversal Algorithms)

##  Giới thiệu

Thuật toán duyệt đồ thị là công cụ quan trọng trong khoa học máy tính, được sử dụng để khám phá cấu trúc gồm các **đỉnh (nodes)** và **cạnh (edges)**.  
Chúng có nhiều ứng dụng thực tế:

- Tìm đường đi ngắn nhất
- Trí tuệ nhân tạo (AI)
- Phân tích mạng xã hội
- Tối ưu hóa luồng hoặc tuyến đường

## Nội dung chính

### Khái niệm cơ bản

- **Đồ thị (Graph)**: Gồm tập hợp các đỉnh và cạnh.
- **Đỉnh (Vertex/Node)**: Một điểm trong đồ thị.
- **Cạnh (Edge)**: Kết nối giữa hai đỉnh.
- **Đồ thị có trọng số**: Các cạnh mang giá trị như chi phí, thời gian...
- **Đồ thị không trọng số**: Các cạnh không mang trọng số.
- **Đường đi (Path)**: Một chuỗi các đỉnh nối nhau qua cạnh.

### Thuật toán Breadth-First Search (BFS)

- **Nguyên lý**: Duyệt theo từng lớp (level). Khám phá các đỉnh gần trước, đỉnh xa sau.
- **Cấu trúc dữ liệu sử dụng**: `Queue`
- **Ứng dụng**:
  - Tìm đường đi ngắn nhất trong đồ thị không trọng số
  - Kiểm tra tính liên thông
  - Tô màu đồ thị hai phía (bipartite graph)
### Ví dụ minh họa
- Đồ thị mẫu 1 (không trọng số) và đường đi BFS từ S đến G.
- Đồ thị mẫu 5 (có trọng số) và đường đi BFS có trọng số từ S đến G.

### Thuật toán Depth-First Search (DFS)

- **Nguyên lý**: Duyệt theo chiều sâu – đi sâu vào một nhánh trước, quay lui nếu không còn đường.
- **Cấu trúc dữ liệu sử dụng**: `Stack` hoặc sử dụng **đệ quy**
- **Ứng dụng**:
  - Tìm tất cả các đường đi giữa hai đỉnh
  - Phát hiện chu trình
  - Sắp xếp tô-pô (Topological Sort)
  - Kiểm tra liên thông mạnh
**Ví dụ**:
- Đồ thị mẫu 1 (không trọng số) và đường đi DFS từ S đến G.
- Đồ thị mẫu 5 (có trọng số) và đường đi DFS có trọng số từ S đến G.

### 🔹 So sánh hiệu suất trên đồ thị lớn

- **BFS (Breadth-First Search)**  
Thường **nhanh hơn và hiệu quả hơn** để tìm đường đi ngắn nhất trong **đồ thị không trọng số** hoặc khi cần duyệt theo từng lớp. Độ phức tạp thời gian: O(V + E) \quad \text{(V: số đỉnh, E: số cạnh)}. Khi mở rộng sang đồ thị có trọng số, BFS vẫn là lựa chọn tốt để tìm đường đi tối ưu.

- **DFS (Depth-First Search)**  
Phù hợp khi cần khám phá toàn bộ nhánh, tìm kiếm theo chiều sâu hoặc kiểm tra cấu trúc logic của đồ thị. Độ phức tạp thời gian: O(V + E). Tuy nhiên, DFS **không đảm bảo tìm đường đi ngắn nhất**, đặc biệt trong đồ thị có trọng số. Khi cần tìm tất cả các đường đi, DFS có thể tốn thời gian hơn đáng kể so với BFS hoặc Dijkstra.