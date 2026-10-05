# Logo xuyên suốt và khung giao diện giả

Hai bộ phận tùy chọn. Deck mẫu đầy đủ: `templates/deck-giao-dien.html` (8 slide).

```html
<link rel="stylesheet" href=".../assets/morph-brand.css">   <!-- logo -->
<link rel="stylesheet" href=".../assets/morph-mock.css">    <!-- khung giao diện -->
...
<script src=".../assets/morph-mock.js"></script>            <!-- trước morph-engine.js -->
```

## 1. Logo xuyên suốt (morph-brand)

Logo nằm trên sân khấu chứ không nằm trong slide nào. Khi chuyển slide, logo bay sang vị trí mới như một diễn viên, nên cả deck liền mạch như một bộ nhận diện.

```html
<div class="deck-stage">
  <div class="brand"><i class="ico" data-icon="leaf"></i><span class="brand-name">Tên đơn vị</span></div>
  <!-- hoặc file logo: <div class="brand"><img src="logo.svg" alt="Tên"></div> -->
  <section class="slide" ...>
```

| Tư thế | Khi nào | Trông thế nào |
|---|---|---|
| `hero` | cover, closing | to, canh giữa phía trên |
| `corner` | mọi slide còn lại | nhỏ ở góc trên bên phải |
| `hide` | quote | trượt lên khỏi khung để câu trích đứng một mình |

- Một slide muốn khác thì ghi `data-brand="hero"`, `"corner"` hoặc `"hide"` trên thẻ `<section>`.
- Đổi vị trí cho hợp style bằng biến, ví dụ đẩy logo xuống trong tấm thẻ của bìa:
  `.deck-stage[data-layout="cover"] { --brand-hero-y: 200px; }`.
  Các biến có sẵn: `--brand-hero-x/y/s/a` và `--brand-corner-x/y/s/a`. Trong đó `s` là tỉ lệ, `a` là điểm neo: `-50%` là canh giữa, `-100%` là mép phải nằm ở x, `0%` là mép trái nằm ở x.
- Góc trái thay cho góc phải: `.deck-stage { --brand-corner-x: 120px; --brand-corner-a: 0%; }`. Nhớ kiểm tra để logo không đè tiêu đề.
- Màu: icon theo `--accent`, tên theo `--fg`. Có thể đổi bằng `--brand-color` và `--brand-name-color`.
- Bìa và slide cuối nên chừa chỗ cho logo, ví dụ `style="padding-top:300px"` trên section.
- `inline-assets.py` nhúng file ảnh logo (png, jpg, gif, webp, svg) vào file cuối, nên deck vẫn chỉ là một file. Ảnh phải nằm trong thư mục deck.

## 2. Khung giao diện giả (morph-mock)

Dùng khi slide cần cho thấy một phần mềm đang chạy mà không muốn dán ảnh chụp màn hình. Khung tự lấy màu theo style: nền sáng hay nền tối đều nổi lên thành một lớp riêng. Riêng terminal luôn nền tối.

| Khung | Lớp | Hợp cho |
|---|---|---|
| Cửa sổ chat | `mock mock-chat` | prompt và câu trả lời của AI, hỏi đáp |
| Terminal | `mock mock-term` | lệnh cài đặt, chạy script |
| Trình duyệt | `mock mock-browser` (`data-url`) | trang web, báo cáo HTML, ảnh chụp trang |
| Điện thoại | `mock mock-phone` | app, chat trên điện thoại (bỏ thanh tiêu đề của khung con) |

Tên trên thanh tiêu đề là `data-title`. Đặt vị trí bằng `style="left:..;top:..;width:..;height:.."` (đơn vị px trên khung 1920x1080).

### Chuyển động

| Lớp | Tác dụng |
|---|---|
| `.type` | chữ gõ từng ký tự. Câu dài tự gõ nhanh hơn để xong trong khoảng 2,6 giây |
| `.lines` | các phần tử con hiện lần lượt từng dòng |
| `.think` | thêm dấu "..." nhấp nháy trước khi các dòng hiện (dùng cùng `.lines`) |
| `.msg.user` / `.msg.ai` | bong bóng của người hỏi (bên phải) và của trợ lý (bên trái); `data-who` ghi tên phía trên |
| `.composer` | ô nhập ở đáy cửa sổ chat; đặt `.type` bên trong để thấy prompt đang được gõ |
| `.cmd` / `.out` | dòng lệnh có dấu nhắc (`--prompt`, mặc định `"$ "`) và dòng kết quả; `.ok`, `.err`, `.hi` tô xanh, đỏ, vàng |

- Trong cùng một khung, các phần chạy **nối tiếp nhau**: câu hỏi gõ xong mới tới câu trả lời. Không cần tự tính thời gian.
- Gắn `data-step` thì phần đó chờ cú bấm, và chuỗi tính lại từ cú bấm. Phím lùi gỡ đúng bước đó (cần `morph-steps.js`).
- Ảnh chụp của `check-deck.py` và `deck.audit()` luôn thấy trạng thái cuối, chữ đầy đủ.

```html
<div class="mock mock-chat" data-title="Trợ lý AI" style="left:1000px;top:250px;width:800px;height:740px">
  <div class="msg user type">Tóm tắt báo cáo thành 3 ý, mỗi ý một câu.</div>
  <div class="msg ai lines think" data-who="Trợ lý" data-step="1">
    <p><b>Tiến độ:</b> ...</p><p><b>Vướng mắc:</b> ...</p><p><b>Tuần tới:</b> ...</p>
  </div>
</div>

<div class="mock mock-term" data-title="Terminal" style="left:120px;top:250px;width:1060px;height:600px">
  <div class="cmd type">git clone https://github.com/andyluu98/slidefly.git</div>
  <div class="out lines"><p>Cloning into 'slidefly'...</p></div>
  <div data-step="1"><div class="cmd type" style="--prompt:'PS> '">...</div></div>
</div>

<div class="mock mock-phone" style="left:1260px;top:120px;width:420px">
  <div class="mock mock-chat"><div class="msg user type">Việc nào đang trễ hẹn?</div></div>
</div>
```

### Luật dùng

- Mỗi slide tối đa **một** khung giao diện. Hai khung cạnh nhau làm người xem không biết nhìn đâu.
- Nội dung trong khung là **ví dụ**: câu trả lời mẫu của AI không được chứa số liệu bịa. Lệnh cài đặt phải lấy từ tài liệu chính thức.
- Khung che hình trang trí của style: nếu thấy thò ra lộn xộn, cho diễn viên đó làm tấm nền phía sau khung, ví dụ
  `.deck-stage:has(.slide.active .mock.plate) [data-actor="card"] { --x: 972px; --y: 222px; --w: 856px; --h: 796px; }`
  rồi gắn thêm lớp `plate` cho khung (cách làm trong `deck-giao-dien.html`).
- Audit tính loại khung vào "diện mạo" của slide: chat, terminal, trình duyệt liền nhau không bị báo nhàm.
