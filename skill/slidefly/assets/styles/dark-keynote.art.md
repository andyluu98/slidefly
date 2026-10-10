# Dark Keynote: luật vẽ minh họa SVG cho từng slide

Dùng cùng `dark-keynote.css`. Lớp sân khấu đã có nền gần đen với lưới 48px, các tấm kính tối biến thành thẻ, vòng tiến độ, chấm lime và con trỏ; file này dạy vẽ **một giao diện SVG inline riêng cho mỗi slide**, như một khoảnh khắc trong video ra mắt phần mềm. Deck mẫu: `gallery/66_demo-dark-keynote.html`.

## 1. Tinh thần
- **Nhân vật là giao diện**, không phải sản phẩm vật lý: cửa sổ, thẻ, ô, thanh trạng thái, con trỏ. Cả sân khấu tối, ánh sáng lạnh, mọi thứ bám lưới và nhịp.
- **Chính xác trước, trang trí sau.** Mọi khối thẳng hàng theo lưới 8px, góc bo 14 đến 28px. Kể chuyện bằng tương phản: lộn xộn (nét đứt, ô rời rạc) rồi một hành động dứt khoát (vào lưới), rồi khoảng trống.
- **Một màu nhấn duy nhất: lime** `#B7F34A`, dành cho điều sản phẩm là hoặc làm: chấm sống, ô đang chọn, tiến độ, con số then chốt. Nếu hai thứ cùng lime thì một trong hai sai. Không dùng màu cảnh báo.
- **Kính giả bằng gradient**: tấm tối ba bậc, viền 1px trắng 10%, mép trên sáng, vệt chéo mờ. Không blur nặng, không `mix-blend-mode`.
- **Nhịp:** hình vào từng nhịp một (khung, đường, ô, nhãn), dứt khoát, không trôi lơ lửng; chuyển động nhanh rồi dừng hẳn.
- **Một ý một hình:** mỗi slide chỉ kể một khoảnh khắc (một hành động, một con số), phần còn lại để tối.
- Khác `neon-cyber` (cyan và magenta, khung HUD), `aurora` (ba ánh sáng màu trôi) và `electric-studio` (hai nửa trắng và xanh đậm): ở đây gần như đơn sắc, một nhấn lime, giao diện thật là nhân vật.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị | Dùng cho |
|---|---|---|
| Nền sân khấu | `var(--bg)` #07080C | khoảng trống |
| Chữ chính, phụ, nhãn | `var(--fg)` #EDF0F7, `var(--muted)` #9AA3B5, `var(--label)` #8791A5 | nhãn mono, chữ |
| Mặt phẳng nổi | `rgba(255,255,255,.03..07)` trên nền tối | thẻ, ô, khung canvas |
| Viền, đường mảnh | `rgba(255,255,255,.10..14)` | hairline, viền thẻ |
| Màu nhấn | `var(--accent)` #B7F34A | một chỗ nổi bật mỗi slide |

- Nét: viền thẻ 1,4px, đường chuyển động 2,6px đầu tròn, vòng mảnh 2,4px. Nét đứt `6 6` cho "ô chưa có" hoặc "tư thế đích".
- Tô bằng **lớp trong `<style>` của deck** (`.dk-card .dk-canvas .dk-bar .dk-hair .dk-ring .dk-slot .dk-path .dk-tile .dk-lit .dk-pill .dk-seg .dk-node .dk-mono`, xem deck mẫu), không ghi `fill="var(...)"` trong thuộc tính, để bản PPTX đọc được. Màu có độ trong (`rgba`) dùng được trong lớp.
- Chữ trong hình chỉ là nhãn mono hoa ngắn (`var(--font-mono)`, 18 đến 20px, giãn 0,14em), tiếng Việt đủ dấu ("TRƯỚC", "SAU", "CỠ CHỮ LỚN"). Không câu dài.
- Cỡ chuẩn: góc bo thẻ 14 đến 28px, ô 44 đến 68px, thanh khung xương cao 10 đến 14px bo tròn hết cỡ, khoảng cách ô 12 đến 16px.
- Mỗi `id` trong SVG (nếu dùng `clipPath`, `linearGradient`) phải duy nhất trong cả deck, đặt tiền tố theo số slide.
- Bóng sáng của chấm lime, vành sáng của rim đã do diễn viên vẽ; trong hình không thêm glow.

## 3. Bộ hình mẫu lặp lại
**Thẻ kính** (một slide thu nhỏ, một thành phần): `<rect class="dk-card" x="30" y="96" width="168" height="104" rx="14"/>`; thẻ đang chọn thêm `dk-on` (viền lime mảnh).
**Ô giao diện** (đơn vị của lưới): `<rect class="dk-tile" width="68" height="68" rx="14"/>`, ô sáng thêm `dk-lit`.
**Ô chưa có** (tư thế cũ, bước kế tiếp): `class="dk-slot"` (nét đứt), có thể là vòng hoặc ô bo góc.
**Đường chuyển động**: một đường cong bậc hai, đầu tròn, vẽ dần: `<path class="dk-path draw" pathLength="1" style="--d:.2" d="M270 450Q370 200 600 220"/>`.
**Thanh khung xương** (thay chữ khi không cần chữ thật): `<rect class="dk-bar" width="210" height="14" rx="7"/>`, phụ `dk-faint`.
**Thanh tiến độ** (ba viên thuốc, viên giữa lime): `<rect class="dk-pill dk-pillon" width="146" height="14" rx="7"/>`.
**Thang đo đoạn**: 12 đoạn rộng 10, cao 46, bo 5; số đoạn sáng là mức (`dk-segon`, trắng 60%), đoạn nhấn `dk-seglime`.
**Điểm dừng**: ô 26px bo 7 (`dk-node`), điểm hiện tại là vòng lime quanh chấm của sân khấu, điểm kế tiếp nét đứt.

## 4. Bốn công thức (khung 1920x1080)
**a. Hình chính cho bìa.**
- Chữ bìa nằm trái (x 120 đến 1040). Tấm kính cửa sổ của sân khấu chiếm x 1100..1800, y 200..760, đèn mép lime ở y 200. Vẽ SVG ở `left:1060px; top:200px`, 740x680, bọc trong `translate(40 0)` để tọa độ khớp cửa sổ.
- Lớp vẽ: thanh tiêu đề (một ô glyph nhỏ và một thanh khung xương, không có nút ba chấm), dải ba thẻ slide bên trái, khung canvas bên phải, đường chuyển động từ ô nhỏ tới ô nét đứt (x 1370..1700, y 420..650). Chấm lime và con trỏ là diễn viên, đã đặt ở (1502, 467) và (1522, 492): chừa trống quanh đó.
- Ô thông báo (diễn viên `panel2`) ngay dưới cửa sổ x 1080..1500, y 745..855: vẽ một vòng nhỏ và hai thanh khung xương lên nó.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).**
- Trên slide `content` (thứ chẵn), tấm kính chiếm x 1240..1810, y 267..997. Chừa dải y 547..717 cho `hl-text`; vòng tiến độ chỉ bật ở slide thứ lẻ.
- Nửa trên: nhãn "TRƯỚC" và "SAU", bốn ô nét đứt rải rác bên trái, mũi tên cong, lưới 2x2 các ô thật bên phải với ô cuối lime. Nửa dưới: đường mảnh và ba viên thuốc tiến độ, viên giữa lime.
- Cùng một thành phần thì cùng hình, đổi chỗ, đổi tư thế.

**c. Quy trình hoặc dòng thời gian.**
- Tấm kính mảnh cao 70px là đường ray ở y 630, đèn rim lime chạy tới điểm hiện tại, chấm lime nằm ở điểm đó (đặt ở x = 136 + i x 342,4).
- SVG đặt chồng (`top:560px`, cao 140): điểm đã qua là ô 26px tối, điểm hiện tại thêm vòng lime r 24, điểm kế tiếp nét đứt, vạch dóng mảnh 20px dưới ray. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ vào vùng chữ của các bước.

**d. Con số hoặc so sánh.**
- Trên slide `stats`, ba tấm kính của sân khấu là ba thẻ x 120..648, 696..1224, 1272..1800, y 365..835; vòng tiến độ và chấm ôm số cuối (nhấn lime).
- Dải đáy y 836..986: mỗi cột (tâm x 384, 960, 1536) một thang đo 12 đoạn sáng 3, 5, 7 đoạn, cột cuối lime, nhãn mono "CỠ CHỮ LỚN, VỪA, NHỎ". So sánh hai phương án: hai thang cạnh nhau cùng độ dài.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: `class="draw" pathLength="1"` và `style="--d:.3"` (cần `morph-motion.css`); thứ tự đúng lưới: khung, đường, ô, nhãn. Không gắn `draw` vào nét đứt.
- Nhãn, thanh khung xương, thang đo: bọc `<g class="reveal">` để hiện sau. Cả hình xong trong khoảng 2 giây.
- Không animation lặp, không rung, không chớp. Thẻ, vòng, chấm, con trỏ chuyển bằng Morph của diễn viên.
- PPTX: `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì xuất thành hình vector; lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.dk-card`), nên giữ tiền tố `dk-`. Chữ trong SVG không sửa được trong PowerPoint: chỉ để nhãn mono ngắn.

## Kiểm trước khi giao
- Mỗi hình đọc được khi tắt hết diễn viên: nếu cần chấm lime mới hiểu, hình chưa đủ ý.
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90..165, không đè dải `hl-text`.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: mỗi slide có đúng một cụm lime (chấm, ô sáng, tiến độ), phần còn lại trắng mờ và xám lạnh.

## 6. Cấm
- Chữ đầy đủ câu trong hình: câu cần sửa được để ngoài SVG, trong hình chỉ có nhãn mono.
- Nút cửa sổ ba chấm màu, thanh menu, dock, logo ứng dụng thật, giao diện của một sản phẩm có thật.
- Hai màu nhấn, màu cảnh báo đỏ, gradient màu mượt, neon tỏa sáng, đường quét HUD (đó là `neon-cyber`).
- Blur nặng, `mix-blend-mode`, bóng đổ đen đậm trong hình.
- Đè hình lên chữ của slide, cho nét chạy qua hàng tiêu đề, hay lấp dải y 547..717 của slide `content`.
- Hình dày đặc: nếu cần hơn sáu khối thì tách slide.
- Số liệu bịa trong nhãn: chỉ dùng chữ ký hiệu hoặc số đã có trong slide.

Phỏng theo lemo-opuscar `styles/dark-keynote/STYLE.md` (MIT) qua MotionFly.
