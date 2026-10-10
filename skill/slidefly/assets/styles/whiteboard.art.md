# Whiteboard: luật vẽ minh họa SVG cho từng slide

Dùng cùng `whiteboard.css`. Lớp sân khấu đã có tấm bảng, vết xước, bóng ma của bài cũ, vòng khoanh cam, bút lông và nam châm bay lơ lửng; file này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, như người thuyết trình đang viết trên bảng. Deck mẫu: `gallery/64_demo-whiteboard.html`.

## 1. Tinh thần
- Cả deck là **một tấm bảng trắng bóng**. Mọi thứ người xem học được đều là nét bút lông khô-xóa được: nét liền một mạch, hơi run, không bao giờ thẳng tuyệt đối.
- **Hình một nét, đơn giản nhất mà vẫn mang ý.** Một câu một hình: hộp, vòng tròn, mũi tên, thước chia vạch, ghim nam châm. Không đổ bóng, không tô loang, không chi tiết tả thực.
- **Không tay, không con trỏ.** Bút và nam châm tự bay. Đừng vẽ bàn tay, cánh tay hay người que cầm bút.
- **Ba màu bút, mỗi màu một nghĩa giữ suốt deck:** đen cho vật và cấu trúc, xanh cho tín hiệu, quy trình, nối kết, cam cho điều quan trọng nhất của slide (mỗi slide chỉ một chỗ cam, như "câu trả lời được khoanh").
- Khác `notebook-tabs` (giấy kẻ, tab màu, ghi chú dán) và `paper-ink` (giấy mực in, chữ serif): ở đây là nét bút trên nền bóng, không giấy, không chữ in.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Biến CSS | Dùng cho |
|---|---|---|
| Bút đen | `var(--ink)` (#23262c) | vật, khung, đường chính |
| Bút xanh | `var(--blue)` (#2a5cb3) | mũi tên, trục, nối, chấm vệt |
| Bút cam | `var(--orange)` (#d97757) | điểm nhấn duy nhất, vòng khoanh |
| Chữ cam đậm | `var(--orange-d)` (#b5502b) | nhãn chữ cam (đủ tương phản trên nền bảng) |
| Nền trạm | `#F7F7F2` | tô trong vòng tròn để che trục phía sau |

- Một độ dày: nét chính **7px**, nét phụ 5px, chấm vệt 9px. `stroke-linecap` và `stroke-linejoin` luôn `round`. Không đổi độ dày trong một hình.
- **Nét tay:** đường đi qua các điểm có lệch vuông góc 1 đến 3px, bước 60 đến 90px. Hình chữ nhật là **bốn nét rời** vượt qua góc 4 đến 7px. Vòng tròn **vẽ quá điểm đầu** (1,15 đến 1,6 vòng, bán kính nở dần), không khép kín.
- Khai báo lớp nét trong `<style>` của deck (`.wb-k .wb-b .wb-o .wb-t .wb-stn .wb-ghost .wb-dot .wb-hand`, xem deck mẫu) để bản PPTX đọc được màu và nét; không ghi `stroke="var(...)"` trong thuộc tính.
- Chữ trong hình dùng `var(--font-hand)` (Patrick Hand), cỡ 32 đến 62px, ngắn một hai chữ ("tư thế A", "tách", "bay!"). Câu cần sửa được để ngoài SVG.
- Nét "bóng ma của bài cũ": nét đen mờ 38% đứt đoạn `stroke-dasharray: 9 12` cho vật ở trạng thái trước.

## 3. Bộ hình mẫu lặp lại
**Hộp bốn nét có vượt góc** (một vật; hộp nghiêng `rotate(-12)` là "tư thế B"):
```svg
<path class="wb-k" d="M36.7 60.1L203.7 60.3M200.4 57.4L198.4 165.4M203.3 159.1L34 159.9M41.1 164.1L40.4 57.1"/>
```
**Mũi tên tay** (thân cong một nét, đầu mở hai nét, xanh cho quan hệ):
```svg
<path class="wb-t" d="M20 120Q92 36 200 60M176.9 66.4L200 60M181.8 44.4L200 60"/>
```
**Chấm vệt** (đường đi của vật: nét tròn đầu, đứt 1 rồi 20): `<path class="wb-dot" d="M138 306C210 340 290 310 316 236"/>`
**Vòng khoanh cam** quanh điều quan trọng (đã có diễn viên `circle` vẽ sẵn ở slide `content`, `stats`, `closing`; trong hình chỉ vẽ thêm khi cần khoanh một chi tiết nhỏ): `<path class="wb-o" d="..."/>`.
**Trạm** (vòng xanh tô `#F7F7F2` đè lên trục), trạm cuối thêm vòng cam và dấu tích:
```svg
<path class="wb-stn" d="M16 49C27 49 37 59 37 70..."/><path class="wb-o" d="M1374 70L1382 79L1395 60"/>
```
**Thước chia vạch**, **chấm đứt đáy** (`.wb-dot` dưới hàng hình để nói "cùng một đường"), **tia cam ngắn** quanh vật chuyển động (ba nét 80px song song).

## 4. Bốn công thức (khung 1920x1080)
**a. Hình chính cho bìa.**
- Chữ bìa nằm trái (x 120 đến 1040). Diễn viên `circle` khoanh sẵn một vòng ở x 1118..1822, y 314..626 (ô 800x400 tâm 1470,470, vòng thực nhỏ hơn 12% và 22%).
- Vẽ SVG trong x 1110..1830, y 290..670 và để hình nằm **trong** vòng, không chạm nét cam.
- Lớp vẽ: vật chính ở phải (deck mẫu: máy bay giấy bốn nét, nếp gấp xanh), bản mờ nhỏ của vật ở trái dưới, chấm vệt xanh nối hai bản, ba nét cam tốc độ sau đuôi, một chữ cam ngắn.
- Vật là ẩn dụ của chủ đề, không phải logo hay sản phẩm thật.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).**
- Trên slide `content`, vùng x 1260..1800, y 280..980. Chừa dải y 555..720 cho `hl-text` và vòng cam của diễn viên: slide `content` thứ chẵn, vòng ôm một dòng chữ (thực y 562..710); slide thứ lẻ, vòng ôm số lớn (thực y 534..682).
- Nửa trên: hai trạng thái của một vật (bản mờ đứt nét, bản đậm nghiêng) nối bằng mũi tên xanh, nhãn chữ tay ở dưới.
- Nửa dưới (y 735..980): ba tư thế liền nhau trên một đường chấm, tư thế cuối viền cam.
- Cùng một vật thì cùng hình dạng (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.**
- Diễn viên `rule` co thành trục bút xanh ở y 630; SVG đặt chồng lên (`top: 560px`, cao 140).
- Trạm thứ i (5 bước) ở x = 136 + i x 342,4, tâm y 630. Giữa hai trạm một cung xanh có đầu mũi tên, cao tối đa 56px so với trục (chữ bước lẻ kết thúc y 578).
- Trạm cuối: vòng cam và dấu tích. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ vào vùng chữ của các bước.

**d. Con số hoặc so sánh.**
- Trên slide `stats` dùng dải đáy y 836..986: mỗi cột (tâm x 384, 960, 1536) một "slide nháp" 200x120 với 3, 5, 7 dòng kẻ mỏng dần.
- Cột cuối có nét cắt cam đứt và chữ "tách"; vòng cam của diễn viên đã khoanh con số cuối.
- So sánh hai phương án: hai hình cạnh nhau cùng kích cỡ, nét đen và nét xanh.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"` (giây trễ), cần `morph-motion.css`. Thứ tự như người viết: vật chính trước, nếp và chi tiết sau, nhãn cuối. Không gắn `draw` vào nét đứt hoặc `.wb-dot`.
- Nhãn, tia tốc độ, bản mờ: bọc `<g class="reveal">` để hiện sau nét. Cả hình xong trong khoảng 2 giây.
- Không animation lặp, không rung. Bút lông, nam châm, tẩy bay bằng Morph của diễn viên.
- PPTX: `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì xuất thành hình vector; lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.wb-k`), nên giữ tiền tố `wb-`. Vòng khoanh và gạch chân của diễn viên dùng `vector-effect: non-scaling-stroke` để giữ nét 7px khi kéo giãn; PowerPoint có thể vẽ nét dày hơn đôi chút ở vòng kéo rất dẹt.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn một hai chữ.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không dính nét cam của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Mọi `id` trong SVG duy nhất trong cả deck (tiền tố theo số slide nếu dùng `pattern` hay `clipPath`).
- Rà màu: chỉ đen, xanh, cam, trắng bảng; chữ cam dùng `var(--orange-d)`.

## 6. Cấm
- Màu ngoài ba bút (đen, xanh, cam), gradient, bóng đổ trong hình, 3D, tô loang như màu nước.
- Bàn tay, cánh tay, con trỏ chuột, người que.
- Đè hình lên chữ của slide, cho nét chạy qua hàng tiêu đề y 90..165, hay chạm vào nét cam của diễn viên `circle`.
- Hai chỗ cam trong một slide (cam là "câu trả lời", chỉ một).
- Chữ tay dài hoặc công thức bịa, số liệu không có nguồn: dùng chữ ký hiệu, số trong deck mẫu hoặc nhãn "ví dụ".
- Hình quá sạch: thước kẻ, đường thẳng tuyệt đối, hình tròn khép kín hoàn hảo.

Phỏng theo lemo-opuscar `styles/whiteboard/STYLE.md` (MIT) qua MotionFly.
