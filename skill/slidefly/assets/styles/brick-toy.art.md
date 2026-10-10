# Đồ chơi lắp ghép: luật vẽ minh họa SVG cho từng slide

Dùng cùng `brick-toy.css`. Mỗi slide đáng nhớ có một hình SVG inline xếp từ chính những viên gạch của style, như một mô hình vừa lắp xong trên bàn. Deck mẫu: `gallery/84_demo-brick-toy.html`.

## 1. Tinh thần
- Cả deck là **một thế giới gạch nhựa nhìn thẳng từ phía trước**, đặt trên mặt bàn sáng, hậu cảnh nhòe. Mọi hình đều xếp từ gạch cứng có núm tròn; gạch chỉ trượt và chồng lên nhau, không uốn cong, không méo.
- **Ngôn ngữ phẳng có độ bóng**: mỗi viên một màu đặc, một dải sáng chữ nhật gọn ở mặt trên (ánh đèn hộp), vệt tối ở đáy nơi hai viên chạm nhau, núm tròn trên mọi mặt trên. Không 3D thật, không đường chéo isometric.
- **Chỉ màu gạch cơ bản**: đỏ, xanh dương, vàng, xanh lá, trắng, đen. Lửa và ánh sáng cũng là gạch (cam, vàng trong suốt), không phải gradient mềm.
- Nhân vật được lắp từ gạch (rô-bốt, tên lửa, màn hình, tháp); không dùng tên hay hình dáng người nhựa của thương hiệu nào, không in chữ lên núm.
- Giọng vui, gọn, rõ cấu trúc: người xem phải đếm được số viên, số hàng.

## 2. Bảng màu, kích thước, chất liệu
| Vai trò | Giá trị |
|---|---|
| Đỏ, xanh dương, vàng | `#c91a09`, `#0055bf`, `#f2cd37` |
| Xanh lá, trắng, đen | `#237841`, `#f2f2ee`, `#1b2a34` |
| Gạch trong suốt (lửa) | `#f26a1b`, `#f59a22`, `#f9c923`, độ mờ 0,9 |
| Chữ nhãn | `var(--black)` (#1b2a34), `var(--font-body)` 800, in hoa, giãn 0,1em, 18 đến 20px |
| Số, chữ cái trong đồng tiền | `var(--font-display)` 800, 24px, trên đĩa trắng `bt-coin` |

- **Quy cách một viên** (khung 1:1): bước núm 80, thân cao 96, núm rộng 48 cao 20, bo 7. Hai viên chồng nhau cách nhau 96 (núm của viên dưới lọt vào viên trên).
- Bóng đổ bằng hình chữ nhật mờ: dải sáng trên `#fff` 30%, mép sáng bên trái 16%, mép tối bên phải 10%, dải tối đáy 20%, viền thân `#1b2a34` 22% dày 1,6px (cho gạch trắng không chìm vào nền sáng).
- Không `filter`, không `mix-blend-mode`. Tỷ lệ phóng cả hình bằng `transform="translate(x y) scale(k)"` bọc quanh hình gạch.
- Khai báo lớp (`.bt-ink .bt-ghost .bt-arc .bt-ar .bt-coin .bt-lb .bt-num`) trong `<style>` của deck để bản PPTX đọc được màu và nét. Gạch tự mang màu bằng thuộc tính `fill`.

## 3. Bộ hình mẫu lặp lại
**Một viên gạch** 2 núm (thân, dải sáng, mép, bóng đáy, hai núm có mũ sáng):
```svg
<rect x="16" y="0" width="48" height="26" rx="8" fill="#0055bf"/><rect x="96" y="0" width="48" height="26" rx="8" fill="#0055bf"/>
<rect x="0" y="20" width="160" height="96" rx="7" fill="#0055bf" stroke="#1b2a34" stroke-opacity=".22" stroke-width="1.6"/>
<rect x="8" y="24" width="144" height="11" rx="4" fill="#fff" fill-opacity=".30"/><rect x="0" y="107" width="160" height="9" rx="4" fill="#000" fill-opacity=".20"/>
```
**Chồng gạch:** vẽ từ dưới lên, mỗi viên sau đặt cao hơn viên trước đúng 96; viên trên che núm viên dưới. **Gạch dốc** (mũi tên lửa): hình thang đáy rộng, đỉnh một núm. **Cửa sổ tròn** (viền xám nhạt, kính xanh đậm, vệt sáng cung). **Mặt rô-bốt**: hai chấm đen có chấm sáng, một cung cười.
**Gạch dốc làm mũi tên lửa và mái:** thân hình thang, đáy rộng bằng số núm, đỉnh một núm:
```svg
<rect x="136" y="0" width="48" height="26" rx="8" fill="#c91a09"/>
<path d="M80 116L120 20Q160 16 200 20L240 116Z" fill="#c91a09" stroke="#1b2a34" stroke-opacity=".22" stroke-width="1.6"/>
```
**Đồng tiền chú thích** (`bt-coin`) đặt cạnh viên gạch, không đè lên núm; nét nối `bt-ink` 2px dài không quá 40px.
**Tấm đệm xanh lá** (tấm nền, dày 1/3 viên, núm đều) cho mặt đất; có thể cắt cao còn 52px để làm đường ray.
**Bóng chạm bàn:** elip dẹt `#1b2a34` 14% dưới chân mô hình.
**Đồng tiền số:** `<circle class="bt-coin" r="17"/>` kèm số hoặc chữ `bt-num`, nối vật bằng nét `bt-ink` 2px.
**Vật ma (tư thế cũ):** cùng hình viên gạch bằng nét đứt xanh (`bt-ghost`), cung bay nét chấm đỏ (`bt-arc`) kết thúc bằng mũi tên đặc `bt-ar` đặt đúng hướng cuối cung.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ nằm trái (x 120 đến 1040); tên lửa phóng lên, bệ phóng, rô-bốt và mặt đất do diễn viên của style dựng ở nửa phải. Hình riêng thêm **một vật mang nghĩa "slide"**: một màn hình xếp từ gạch (khung vàng, hai hàng giữa là ô cửa xanh có tranh: mặt trời, mây, đồi, mái nhà) đứng ngay trên viên gạch đỏ của diễn viên `b1` (deck mẫu: x 1082, y 695, tỷ lệ 0,55; đáy màn hình trùng đỉnh thân `b1` ở y 917).
- SVG phủ cả khung 1920x1080 để căn chính xác với diễn viên.
- Không đè lên tiêu đề (x lớn nhất khoảng 1010).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 270 đến 990). Chừa dải y 600 đến 660 cho `hl-text`. Nửa trên: một viên gạch xanh ở hai tư thế (vật ma nét đứt ở trên trái, viên đặc gắn trên viên đỏ lớn), cung bay có mũi tên, ba nét nhỏ báo tiếng "tách" ở chỗ khớp, hai ô chữ A, B, ba đồng tiền số 1, 2, 3 chỉ vào viên gạch, cung bay, chỗ khớp. Nửa dưới: ba viên gạch (xanh, vàng, đỏ) xếp hàng làm bảng chú thích, mỗi viên một số và nhãn ngắn bên dưới.
- Phần nửa trên không vượt y 300 của SVG.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; diễn viên `ground` thu thành đường ray (cao 52px, y 612) mang các núm. **Ẩn chấm trạm mặc định** (`.s-tl .step::before { display: none; }`) và đặt mỗi trạm một viên gạch 3 núm đứng trên thân ray (x = 131 + i × 342,4 với 5 bước, tỷ lệ 0,34, cao khoảng 39px nên đỉnh núm ở y 593). Các cặp mũi tên trắng đôi nằm trên thân ray giữa hai trạm. Màu theo thứ tự đỏ, xanh dương, vàng, xanh lá, đen (trạm cuối).
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên `stats`, dải đáy y 836 đến 986: mỗi cột một chồng gạch **càng nhiều ý, viên càng nhỏ và càng nhiều**: 3 viên (tỷ lệ 0,45), 5 viên (0,27), 7 viên (0,19). Cột "nên tách slide" xẻ chồng 7 viên thành hai chồng 4 và 3, ngăn bằng đường đứt dọc và hai mũi tên ra hai bên. Tâm cột x 384, 960, 1536 (264, 840, 1416 khi SVG ở left 120); mỗi chồng có bóng elip dưới chân.

## 5. Chuyển động và xuất PPTX
- Hình xếp xong hiện bằng `<g class="reveal">`; nét vẽ dần `draw` chỉ dùng cho đường liền (dây, cung) và cần `morph-motion.css`. Nét đứt, nét chấm không gắn `draw`.
- Không animation lặp. Gạch bay vào và chồng lên nhau đã là việc của diễn viên.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.bt-ghost`), nên dùng lớp có tiền tố `bt-`; màu gạch để thuộc tính `fill`. Dùng `scale` trong `transform` của nhóm `g` là được.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn (A, B, số, một đến hai từ).

## Thứ tự lớp trong một hình
1. Bóng chạm bàn (elip mờ) nằm dưới cùng.
2. Gạch xếp từ dưới lên: viên sau che núm viên trước.
3. Vật ma, cung bay và mũi tên.
4. Đồng tiền số, chữ nhãn nằm trên cùng.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: gạch không chạm chữ, không vào hàng tiêu đề, không đè lên núm hay thân của gạch diễn viên (trừ chỗ đã tính, như màn hình đứng trên `b1`).
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`.
- Đếm lại: số viên trong chồng bằng số ý của cột; núm của mỗi viên bằng số bước rộng; hai viên chồng nhau khớp nhau đúng một bước núm.

## 6. Cấm
- Màu ngoài sáu màu gạch (và cam, vàng trong suốt cho lửa); gradient màu, bóng đổ mềm, ánh phát quang, hiệu ứng 3D hay isometric.
- Tên, logo, hình người nhựa của thương hiệu thật; in chữ hay biểu tượng lên núm; gạch có chữ ký hãng.
- Gạch bị uốn, co giãn, xoay méo; hai viên chồng lệch bước núm.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Ghi số đo hay số liệu bịa vào hình: dùng chữ ký hiệu (A, B, 1, 2, 3) hoặc số đúng như nội dung slide.

Phỏng theo lemo-opuscar `styles/brick-toy/STYLE.md` (MIT) qua MotionFly.
