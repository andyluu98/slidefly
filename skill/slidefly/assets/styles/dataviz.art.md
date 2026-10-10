# Dataviz: luật vẽ minh họa SVG cho từng slide

Dùng cùng `dataviz.css`. Lớp sân khấu đã có giấy kem chấm lưới, khung biểu đồ, dải màu "warming stripes", thước trục, cây bút chì đỏ xanh; file này dạy vẽ **một biểu đồ SVG inline riêng cho mỗi slide**, như một hình trong bài báo dữ liệu. Deck mẫu: `gallery/65_demo-dataviz.html`.

## 1. Tinh thần
- **Biểu đồ là nhân vật.** Mỗi hình là một phép biểu đồ có nghĩa: một điểm rơi xuống, một đường nối, một trục mọc ra, một ô trống chờ giá trị. Chọn loại biểu đồ theo ý của slide: so sánh hạng mục dùng cột, thay đổi theo thời gian dùng đường, trước và sau dùng biểu đồ độ dốc, đếm đơn vị dùng ô hoặc chấm.
- **Màu mã hóa đúng một thứ: giá trị.** Dải xanh đậm, xanh nhạt, trắng ngà, cam nhạt, cam, đỏ chạy từ thấp lên cao. Mọi thứ khác (trục, lưới, chữ) là mực nâu đen trên giấy kem. Giá trị nhạt thì để nhạt, không kéo dải màu cho "kịch tính".
- **Chú thích ghim vào dấu.** Một dòng chữ viết tay xanh, một đường dẫn lượn, kết thúc bằng vòng **không khép kín** quanh điểm cần chú ý. Mỗi hình tối đa một chú thích.
- **Không bịa số.** Trục chỉ có vạch, không có chữ số; số liệu thật chỉ là số đã có trong slide. Hình minh họa ý (không phải dữ liệu đo) phải ghi nhãn "minh họa, chưa có số liệu" bằng chữ mono nhỏ.
- Khác `cartesian` (đường kẻ mảnh, vòng tròn compa trên giấy can) và `bento-light` (thẻ trắng bo góc trên nền xám): ở đây là giấy kem, mực đậm, dải màu giá trị và bút chì.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Biến CSS | Dùng cho |
|---|---|---|
| Mực | `var(--ink)` (#2A2621) | trục, đường chuỗi số, viền chấm |
| Chữ phụ, nhãn | `var(--muted)` (#5E5648) | nhãn mono, chữ trục |
| Giấy tờ | `var(--sheet)` (#FBF8F0) | khung biểu đồ, ô khung |
| Bút xanh | `var(--blue)` (#2166AC), chữ `var(--blue-t)` | ghi chú, mũi tên, vòng ghim |
| Dải giá trị | `var(--r0)` tới `var(--r6)` | xanh đậm, xanh nhạt, ngà, cam nhạt, cam, đỏ |

- Nét: đường chuỗi 3,2px, trục 2,4px, vạch mảnh 2px, lưới 1,4px (`--grid`), đường chuẩn đứt `9 8`. Đầu nét tròn.
- **Chấm dữ liệu có viền mực 2,2px** để giá trị nhạt vẫn thấy trên giấy kem. Cỡ chấm 11 đến 21px.
- Khai báo lớp trong `<style>` của deck (`.dv-d .dv-r0..r6 .dv-line .dv-ax .dv-hair .dv-mean .dv-lead .dv-fr .dv-slotd .dv-mono .dv-hand`, xem deck mẫu), tô bằng class chứ không ghi `fill="var(...)"`, để bản PPTX đọc được.
- Chữ nhãn dùng `var(--font-mono)` (IBM Plex Mono) 18 đến 20px; chú thích viết tay dùng `var(--font-hand)` (Patrick Hand) 36px, tiếng Việt đủ dấu.
- Khung `plot` của sân khấu: trục đứng ở 6,5% bề rộng tính từ trái, trục ngang ở 91,3% chiều cao tính từ trên, năm đường lưới chia đều; hình đặt trùng khung dùng đúng các mốc này.
- Mỗi `id` trong SVG (nếu dùng `pattern`, `clipPath`) phải duy nhất trong cả deck, đặt tiền tố theo số slide.
- Một hình dùng tối đa ba sắc độ của dải giá trị; chấm đỏ đậm dành cho điểm quan trọng nhất của slide.

## 3. Bộ hình mẫu lặp lại
**Chấm dữ liệu** (màu theo giá trị): `<circle class="dv-d dv-r5" cx="310" cy="205" r="12"/>`.
**Chuỗi đường nối chấm** (một nét tay, vẽ dần): `<path class="dv-line draw" pathLength="1" style="--d:0" d="..."/>`.
**Đường chuẩn** (giá trị tham chiếu) và nhãn: `<path class="dv-mean" d="M45 240H675"/><text class="dv-mono dv-sm" x="62" y="230">chuẩn</text>`.
**Ghi chú ghim vào điểm**: chữ viết tay, đường dẫn lượn, vòng không khép:
```svg
<text class="dv-hand" x="64" y="56">một vật, nhiều tư thế</text>
<path class="dv-lead" d="M344 58C430 74 520 100 574 126"/><path class="dv-lead" d="M628 150C640 120 610 112 592 128..."/>
```
**Ô trống kế tiếp** (giá trị chưa biết): vòng hoặc ô nét đứt `class="dv-slotd"`, đặt ngay sau điểm cuối.
**Biểu đồ độ dốc**: hai trục đứng cách nhau 280px, mỗi hạng mục một chấm ở hai đầu nối một đoạn thẳng, số thứ tự mono bên trái.
**Biểu đồ đơn vị**: hàng chấm cùng cỡ (3, 5, 7 chấm), chấm mất đi thành vòng đứt khi muốn nói "thừa". Cỡ chấm co lại nếu muốn mã hóa thêm một đại lượng.

## 4. Bốn công thức (khung 1920x1080)
**a. Hình chính cho bìa.**
- Chữ bìa nằm trái (x 120 đến 1040). Diễn viên `plot` là khung biểu đồ x 1100..1800, y 250..730: trục đứng x 1145, trục ngang y 688, lưới y 330, 410, 490, 570, 650. Dải `stripes` nằm ngay dưới (y 759..817).
- SVG đặt trùng khung (`left:1100px; top:250px`, 700x480), vẽ trong tọa độ khung: một chuỗi 5 đến 7 điểm nối bằng một nét, chấm tô theo giá trị, đường chuẩn đứt, một chú thích ghim vào điểm cuối (điểm cao nhất, đỏ). Nhãn "minh họa, chưa có số liệu" ở góc dưới trái.
- Cây bút chì của sân khấu chỉ vào điểm cuối từ phía dưới phải: chừa trống vùng x 1640..1800, y 420..700.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).**
- Trên slide `content`, khung `plot` chiếm x 1240..1810, y 267..997 (slide thứ chẵn). Chừa dải y 547..717 cho `hl-text`.
- Nửa trên (y 300..530): biểu đồ độ dốc giữa hai trạng thái (tư thế A và B) của 3 đến 5 thành phần, mỗi thành phần một chấm màu và một đoạn nối.
- Nửa dưới (y 735..935): ba khung nhỏ liên tiếp, cùng một chấm đổi chỗ, chấm cuối đỏ, mũi tên xanh giữa các khung. Cùng một vật thì cùng chấm (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.**
- Diễn viên `axis` thành thước trục y 630 (x 120..1800). SVG đặt chồng (`top:560px`, cao 140). Trạm thứ i (5 bước) ở x = 136 + i x 342,4, tâm y 630: chấm giá trị cỡ 15px, màu đi từ xanh đậm tới đỏ, vạch dóng ngắn 20px dưới trục.
- Chấm cuối có vòng ghim không khép; ô nét đứt ở x 136 + 5 x 342,4 là "ô tiếp theo chưa biết". Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.**
- Trên slide `stats`, diễn viên `grid` đã trải giấy kẻ dòng sau các con số. Dải đáy y 836..986: mỗi cột (tâm x 384, 960, 1536) một hàng chấm theo số ý (3, 5, 7), cùng màu theo giá trị, chấm càng nhỏ khi càng nhiều ý; hai ô cuối ở cột cuối thành vòng đứt ("nên tách").
- Dưới hàng chấm: một đường nền mảnh và nhãn mono ("cỡ chữ lớn", "vừa", "nhỏ"). So sánh hai phương án: hai hàng cạnh nhau, cùng thang, cùng trục.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"`, cần `morph-motion.css`. Thứ tự đúng phép biểu đồ: chuỗi nét trước, chấm sau, ghi chú cuối. Không gắn `draw` vào nét đứt (đường chuẩn, `dv-slotd`).
- Chấm, nhãn, chú thích: bọc `<g class="reveal">` để hiện sau nét. Cả hình xong trong khoảng 2 giây.
- Không animation lặp, không đổi màu liên tục. Các hộp lưới, dải màu, bút chì chuyển bằng Morph của diễn viên.
- PPTX: `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.dv-d`), nên giữ tiền tố `dv-`. Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn mono ngắn và một ghi chú.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90..165, không đè chữ `hl-text`.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: màu chỉ có ở chấm hoặc cột mã hóa giá trị, vòng ghim và chữ chú thích xanh; còn lại là mực.
- Rà số liệu: không có chữ số trên trục, không có số bịa trong nhãn.

## 6. Cấm
- Màu trang trí không mã hóa giá trị, gradient mượt, bóng đổ, 3D, biểu đồ tròn, ba trục.
- Kéo giãn dải màu cho giá trị nhạt trông lớn; tô đỏ vì "đẹp".
- Số liệu, tên nguồn hay thương hiệu có thật khi slide không cung cấp; con số trên trục khi chưa có dữ liệu.
- Đặt hình đè lên chữ của slide, cho nét chạy qua hàng tiêu đề, hay chạm vào dải y 547..717 của slide `content`.
- Hình dày đặc: một hình một ý; chú thích dài thay cho chú thích một dòng.

Phỏng theo lemo-opuscar `styles/dataviz/STYLE.md` (MIT) qua MotionFly.
