# Find shortest path using A* algorithm

- Chương trình ứng dụng thuật toán A* để tìm đường đi tối ưu về quãng đường giữa 2 điểm trên một bản đồ địa hình cho trước (Grayscale), sau đó vẽ đường đi tìm được trên bản đồ đã cho đồng thời cho biết độ dài quãng đường và tổng số điểm đã tương tác trên bản đồ.
- Nội dung mô tả đồ án chi tiết được viết trong file `Project01.pdf`.
- Giải thích chi tiết về chương trình, **các hàm heuristics** được viết trong file `/Report/Report.pdf`.
- Phần source code được để trong file `/Source`.

## Installation

Cần cài đặt Python3 và thư viện OpenCV.

```bash
  pip install opencv-python
```
    
## Usage

- Trong xử lý ảnh, quy ước **trục ngang sẽ là y** và **trục dọc sẽ là x**. Gốc tọa độ sẽ nằm ở phía trên cùng bên trái

- Bản đồ input (map.bmp) phải ở dạng **Grayscale** và phải được đặt cùng vị trí với 2 file source code.

- File input.txt gồm 3 dòng, dòng đầu tiên là tọa độ điểm xuất phát, dòng thứ hai là tọa độ điểm đích, dòng cuối là tham số m - ``Project01.pdf``

- Sau khi có đầy đủ 2 file input và run thì chương trình sẽ vẽ đường đi tìm được trên bản đồ đã cho đồng thời cho biết độ dài quãng đường và tổng số điểm đã tương tác trên bản đồ.

- Trong trường hợp không tìm được path thì chương trình sẽ thông báo

## Authors

- [Ngô Huy Anh - 19CLC6 - FIT HCMUS](https://github.com/tristanhuyanhngo)
- [Triệu Nguyên Phát - 19CLC6 - FIT HCMUS]()
