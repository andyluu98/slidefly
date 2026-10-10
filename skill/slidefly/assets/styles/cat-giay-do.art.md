# Cắt giấy đỏ: luật vẽ minh họa (lớp minh họa của `cat-giay-do.css`)

Dùng khi deck chọn style `cat-giay-do` và cần một minh họa SVG inline vẽ riêng cho từng slide theo nội dung. Lớp sân khấu (diễn viên trong file CSS) lo phần trang trí chung; file này lo hình vẽ mang ý của slide.

## 1. Tinh thần

- Mọi thứ là **một tờ giấy đã cắt bằng kéo** rồi đặt phẳng lên tờ giấy khác. Không tô bóng, không viền nét, không gradient: chi tiết, khối và biểu cảm chỉ đến từ **phần bị cắt bỏ**. Lỗ thủng là chỗ nền kem lộ ra.
- Giấy đỏ là vật liệu chính; nền là giấy kem hoặc vàng nhạt. Nền và hình phải khác họ giấy: đỏ đặt trên đỏ thì hình dính thành một mảng.
- Chiều sâu bằng **tông giấy cách nhau một bậc** (xa thì đỏ nhạt, gần thì đỏ chính, vật nặng thì đỏ thẫm) và một bóng giấy mỏng, sát.
- Hoa văn dân gian, đối xứng gấp: bông tròn 8 cánh gấp từ một múi 45 độ, mây cuộn, sóng nước vảy, hoa mai, răng cưa, trăng lưỡi liềm. Nếp gấp mờ để lại là thật với nghề, cứ giữ.
- Vàng kim chỉ cho **một điểm nhấn** mỗi slide (bông mai, con số quan trọng nhất), không thành màu chính thứ hai.

## 2. Bảng màu, nét, chất liệu

| Vai | Biến CSS | Dùng cho |
|---|---|---|
| Giấy đỏ chính | `var(--pc-red)` | hình chính, mảnh gần |
| Đỏ thẫm | `var(--pc-deep)` | mảnh nặng, cuống nối, nước |
| Đỏ nhạt | `var(--pc-pale)` | mảnh xa (mây, đồi) |
| Vàng kim | `var(--pc-gold)` | một điểm nhấn: bông mai, dấu "đề xuất" |
| Giấy kem | `var(--pc-paper)` | nền; nét "đường kéo" cắt xuyên qua giấy đỏ |
| Bóng giấy | `var(--pc-shadow)` | bản sao lệch của mảnh, nằm dưới |
| Chữ | `var(--fg)`, `var(--muted)`, `var(--accent)` | nhãn đặt ngoài SVG |

- **Không có nét viền.** Đường duy nhất được phép dùng `stroke` là: cuống nối giữa các mảnh (đỏ thẫm, dày 6 đến 8px, đầu tròn), đường kéo cắt (kem, 2 đến 3px), nếp gấp (đỏ hồng `#F08A6E`, độ mờ 0,5, dày 1 đến 1,5px).
- **Lỗ thủng:** gom vỏ ngoài và mọi lỗ vào **một `<path>` với `fill-rule="evenodd"`**; các lỗ không được chồng lên nhau (chồng nhau thì evenodd lật lại thành giấy).
- **Không có đảo nổi:** một vòng cắt kín làm rơi phần giữa. Vòng viền trong (đường chỉ âm sát mép) phải chia thành nhiều cung, chừa cầu nối.
- **Bóng giấy:** vẽ cùng path hai lần, lần đầu lớp `pc-sh` dịch `translate(2 3)` (to thì 4 đến 6px), lần sau là màu giấy. Không dùng `filter` blur.
- Viết màu bằng lớp CSS trong `<style>` của deck (`.pc-r { fill: var(--pc-red) }`), không viết `fill="var(...)"` trong thuộc tính: trình xuất PPTX chỉ đổi biến CSS khi màu nằm trong lớp hoặc `style`.

## 3. Bộ hình mẫu

Toạ độ tính quanh tâm (0,0), bọc trong `<g transform="translate(cx cy)">` khi đặt.

**Mép răng cưa** (vỏ ngoài của bông tròn, huy chương, ô cửa sổ): đa giác bán kính xen kẽ, ví dụ 72 răng giữa r 99 và r 94.

**Bông tròn 8 cánh** (biểu tượng của style, dùng cho "một vật", "trung tâm", "chu kỳ"): vỏ răng cưa; 8 cung chỉ âm ở r 86 có cầu nối; 16 trăng lưỡi liềm ở r 73; 8 cánh lá thủng từ r 34 tới r 63 xen 8 hình thoi ở r 56; 8 chấm ở r 25; lỗ tâm r 13 rồi dán bông mai vàng lên.

```svg
<path class="pc-sh" transform="translate(2 3)" fill-rule="evenodd" d="M99 0 L94 4 ... Z M30 -8 Q46 -16 62 -4 Q46 0 30 -8 Z ..."/>
<path class="pc-r" fill-rule="evenodd" d="(cùng path)"/>
```

**Lá thủng (cánh, gân):** thấu kính hai đầu nhọn giữa hai điểm, rộng nhất ở giữa: `M x0 y0 Q cx1 cy1 x1 y1 Q cx2 cy2 x0 y0 Z`.

**Trăng lưỡi liềm:** cung tròn có bề dày thuôn về hai đầu (hai cung lệch tâm), dùng làm vảy cá, sóng, vòng trang trí.

**Mây cuộn:** hợp của 3 đến 4 vòng tròn trên một đáy phẳng, trong mỗi vòng khoét một lưỡi liềm cuộn; dọc đáy là 3 khe chỉ âm có cầu nối. Mây đôi thì lật gương `scale(-1 1)`.

**Bông mai vàng:** 5 cánh elip quanh tâm, mỗi cánh một gân thủng, 5 chấm nhụy và một lỗ tâm. Là mảnh dán đè, được phép nằm trên mảnh đỏ.

**Dải răng cưa** (trục, đường dẫn, viền): băng đỏ cao 36 đến 40px, răng cưa hai mép, hàng lỗ tròn và thoi xen kẽ ở giữa, một đường kéo kem chạy dọc.

**Sóng nước:** hàng vòm nông (dây cung 80, cao 20) màu đỏ thẫm, trong mỗi vòm hai lưỡi liềm đồng tâm.

## 4. Bốn công thức

Khung 1920×1080. Chữ luôn nằm ngoài SVG; SVG đặt `position:absolute` bằng `style="left:..px; top:..px"` và có `width`, `height` (thiếu một trong các thứ này thì trình xuất PPTX bỏ qua hình).

**A. Hình chính cho bìa.** Một bông tròn lớn 600 đến 700px (r 300) ở nửa phải (x 1080..1780, y 180..860), chữ dồn trái (lề trái 200px, chừa phải 920px). Lớp: mây đỏ nhạt ở hai góc chéo phía sau, bông tròn đỏ có vòng lỗ dày hơn bình thường (96 răng, thêm vòng chấm), 4 nếp gấp mờ qua tâm, bông mai vàng ở tâm. Lưu ý: diễn viên `rosette`, `cloud2`, `mai2` của bìa nằm gần đó; hình tròn nên góc vuông của SVG trống, không che diễn viên.

**B. Sơ đồ khái niệm (3 đến 5 thành phần).** Một bông tròn ở giữa là "khái niệm gốc"; mỗi thành phần là một huy chương răng cưa r 60 đến 64, khoét một hình tượng (mũi tên chữ thập, hai hình vuông lồng nhau, nửa vàng nửa đỏ...). Nối bằng cuống đỏ thẫm có lớp `draw`. Trong slide `content`, đặt gọn trong vùng x 1260..1800, y 270..990 (slide chẵn có vùng này trống), nhãn ghi bằng `<p>` đặt tuyệt đối ngay dưới hoặc cạnh từng huy chương, câu chốt ở đáy vùng. Lưu ý: dùng `style="left:..px; width:..px"` cho `.bullets` để bản PPTX không kéo chữ sang vùng hình.

**C. Quy trình hoặc dòng thời gian.** Trong slide `timeline`, một dải răng cưa cao 80px phủ đúng trục y 590..670 (chữ bước lẻ kết thúc ở y 578, bước chẵn bắt đầu ở y 682), mỗi bước một bông mai vàng đúng tâm chấm bước (x = 120 + 16 + i × 342,4 với 5 bước), đường kéo kem chạy dọc dải có lớp `draw`. Ẩn trục và chấm mặc định của slide đó (`.timeline::before, .step::before { opacity: 0 }`). Diễn viên `rosette` và `mai` đã giữ hai đầu trục.

**D. Con số hoặc so sánh.** Mỗi con số một ô cửa sổ cắt giấy vuông 150px đặt trên cột của nó (tâm x 384, 960, 1536 với 3 cột), cao y 250..426; trong ô khoét các khe như dòng chữ, số khe hoặc độ dày khe kể đúng ý của con số (ít ý thì khe dày, nhiều ý thì khe mảnh). Một bông mai vàng nhỏ đánh dấu cột đáng chú ý. Hạ khối `.stats` xuống (`top: 400px`) để số không chạm hình. Không vẽ cột biểu đồ có số nếu không có nguồn.

## 5. Chuyển động

- Chỉ chạy khi slide active, viết theo `.slide.active ...` trong `<style>` của deck.
- Mở gấp: bông tròn phóng từ 0,15 và xoay từ -90 độ về 0 trong khoảng 1,1 giây (`transform-box: fill-box; transform-origin: center`), như tờ giấy vừa mở ra.
- Bật mảnh: bông mai, ô cửa sổ hiện bằng `steps(2, end)`, vượt 1,15 lần trong một nhịp rồi về 1, giật như hoạt hình cắt giấy 12 hình mỗi giây; lệch nhau bằng `--d`.
- Vẽ nét: cuống nối, đường kéo, nếp gấp dùng lớp `draw` có sẵn (thêm `pathLength="1"`, trễ bằng `style="--d:.2"`).
- CSS animation đặt trên một `<g>` **không có** thuộc tính `transform`; bọc thêm một `<g transform="translate(...)">` bên ngoài, nếu không animation sẽ xóa phép dời.
- Có `@media (prefers-reduced-motion: reduce)` tắt mở gấp và bật mảnh.

**Khi xuất PPTX:** SVG inline thành ảnh vector (PowerPoint 365), hiện dần hoặc quét theo lớp `draw`. Animation CSS không sang. Chữ trong SVG không sửa được, nên nhãn để ngoài SVG. Khi dời chữ của bìa sang trái trong `<style>` của deck, viết `.deck-stage .slide[data-layout="cover"] { padding: ...; text-align: left }` (đủ độ ưu tiên để thắng luật của style) thì bản PPTX cũng đặt chữ bên trái, không đè hình.

## 6. Cấm

- Màu ngoài bảng trên; vàng kim nhiều hơn một điểm nhấn mỗi slide; đỏ đặt thẳng lên đỏ cùng tông.
- Nét viền quanh hình, tô bóng gradient, khối 3D, phối cảnh: các lớp giấy luôn song song mặt màn hình.
- Chữ trong ảnh, chữ vẽ bằng path; mọi chữ là HTML dùng `var(--font-display)` (Spectral) hoặc `var(--font-body)` (Lexend).
- Lỗ chồng lỗ, vòng cắt kín tạo đảo nổi, `filter` blur, `mix-blend-mode`, ảnh bitmap nhúng.
- Chép hoa văn của nghệ nhân hay tác phẩm có thật: mọi họa tiết sinh từ hình học (múi gấp, lặp xoay).
- Hình đè lên chữ hoặc lấn vào hàng tiêu đề y 90..165.

Nguồn: Phỏng theo lemo-opuscar `styles/papercut-red/STYLE.md` (MIT) qua MotionFly.
