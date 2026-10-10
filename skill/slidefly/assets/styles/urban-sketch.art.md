# Ký họa đô thị: luật vẽ minh họa SVG cho từng slide

Dùng cùng `urban-sketch.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một trang sổ ký họa vẽ ngay tại chỗ. Deck mẫu: `gallery/79_demo-urban-sketch.html`.

## 1. Tinh thần
- Cả deck là **một trang sổ ký họa trên giấy cold-press màu kem**: nét bút mực nâu sepia mảnh, run nhẹ, thừa ra ở góc, đứt giữa chừng; màu nước loãng đổ lên sau và **lệch khỏi nét** vài pixel.
- **Hai lớp luôn tách rời**: mực (một màu duy nhất, không bao giờ đổi) và màu (ít sắc, pha ngay trên trang). Không có hình nào chỉ có màu mà không có nét.
- Màu **gợi chứ không tả**: vài vệt cửa sổ thay cho cả lưới ô, vài vòng cung răng cưa thay cho cả tán cây. Chừa **trắng giấy** cho mây, chỗ sáng; trắng giấy là giá trị sáng nhất, không bao giờ tô.
- Có thể chỉ để mực, màu xuất hiện như một sự kiện: trong deck mẫu, quả bóng đỏ là vật duy nhất có màu rực.
- Giọng điệu: thân mật, ghi chú viết tay bên lề. Không vẽ người; vật là nhà phố, cây, bóng bay, bút, giá, trang giấy.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (mọi nét) | `var(--ink)` #3B2E25, độ dày 2,6 (nét chính), 1,6 (chi tiết), 2 (nét đứt) |
| Giấy | `var(--paper)` #F3EAD6; tờ vẽ trong hình #FBF6E8 |
| Trời, nước | #9FBCD6 (viền khô #7B9DBA) |
| Đá, tường nhạt | #D8C6A0; hồng đất #D99A7C; xanh khói #A9BFC9 |
| Lá | #7FA04A, lá đậm #58763A, lá non #B2C46A |
| Mái, mái hiên, bóng đỏ | #B8483E, bóng bay #C8452F |
| Ánh đèn | #E2B04A; bóng đổ pha tím xám #8B86A8 (alpha .2) |

- **Màu lệch nét:** gom mọi mảng màu vào một nhóm `<g filter="url(#...)" transform="translate(5 4)">`, vẽ mực ngoài nhóm đó. Lệch 4 đến 6px, cho phép tràn ra ngoài nét.
- **Bộ lọc màu nước** (mép loang, hạt giấy), đặt tên id riêng cho từng SVG (`usA1`, `usA2`...) vì mọi SVG chung một tài liệu:
  `feTurbulence` tần số .035 + `feDisplacementMap` scale 4 đến 6 làm mép nhòe, rồi `feTurbulence` .55 qua `feColorMatrix` thành hạt nâu mờ, `feComposite in` và `feMerge`. Bản PPTX bỏ qua bộ lọc nên hình vẫn đọc được khi phẳng.
- Mảng màu alpha .5 đến .85 (lớp CSS `us-sky us-leaf us-pink us-red us-teal us-lit us-stone us-vio`), viền khô đậm hơn 30 đến 40% ở rìa chỗ cần "đọng sắc tố".
- Chữ viết tay: `var(--font-hand)` (Patrick Hand), 26 đến 34px, chỉ nhãn rất ngắn ("trang 1", "diễn viên", "A", "B"). Số thứ tự trong vòng tròn mực. Chữ có dấu lấy font này (đã có bộ tiếng Việt).
- Khai báo các lớp `.us-k .us-t .us-g .us-d .us-sheet .us-tape .us-hand ...` trong `<style>` của deck (xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Hình mẫu lặp lại
**Nét mực run** (đường thẳng chia nhỏ mỗi 45px, mỗi đoạn lệch ngang 1px, thừa ra 3 đến 8px ở hai đầu, không bao giờ khép kín):
```svg
<path class="us-k draw" pathLength="1" style="--d:0" d="M92 392Q210 394 330 391L616 392"/>
```
**Ô cửa lệch màu** (mực trước, màu lệch sau):
```svg
<g filter="url(#usA1)" transform="translate(5 4)"><path class="us-teal" d="M300 270l34 0 0 52-34 0z"/></g>
<path class="us-k" d="M300 270l34 1 0 52-35 0 1-53M317 270v52M300 296h34"/>
```
**Tư thế bóng ma** (nét đứt, không màu) cho "trước khi di chuyển": `<path class="us-g" d="..."/>`; đường đi bằng chấm `us-d` có mũi tên mực.
**Dấu hiệu lực vô hình** (gió, chuyển động) vẽ bằng các vòng cuốn mực: `M262 262C292 226 322 300 352 262` kèm mũi tên nhỏ ở cuối.
**Băng giấy** (washi tape) giữ trang: `<path class="us-tape" d="M-50 -13l6 6.5-6 6.5 6 6.5-6 6.5H44l6-6.5-6-6.5 6-6.5-6-6.5z"/>`, đặt ở hai góc trên của tờ giấy, xoay vài độ.
**Vệt thử màu** (swatch) và **bắn mảng màu** (vài chục chấm nhỏ cùng bảng màu) để chuyển cảnh từ hình sang lề giấy. **Bóng bay đỏ** là vật chính duy nhất mang màu rực, có chút giấy trắng chừa làm điểm sáng.
**Vòng số**: `<circle class="us-bal" r="19"/>` kèm số viết tay, dẫn bằng một nét mảnh `us-t`.
**Tán cây**: nền lá nhạt rồi 100 đến 150 chấm lá (`<ellipse rx="6..12" ry="4..8">`, xoay ngẫu nhiên), chấm tối ở góc dưới phải, sáng ở góc trên trái; viền mực chỉ là vài cung răng cưa ngắn ở rìa, không vẽ hết chu vi.
**Mây**: không tô; chừa giấy trắng (`fill: var(--paper)`), đáy mây pha xám xanh alpha .45.

## Diễn viên của style và vai của chúng quanh minh họa
| Diễn viên | Vai | Gợi ý khi vẽ hình |
|---|---|---|
| `sky` | vệt trời nhạt dần xuống | hình đặt lên vệt này, không vẽ thêm trời |
| `row` | dải nhà phố (mực + màu lệch) | hình chính không vẽ lại nhà phố; chỉ vẽ vật khác |
| `ground` | nét mặt đất, thành trục thời gian ở slide `timeline` | căn trạm theo y 630 |
| `swatch` | dải vệt thử màu dưới tiêu đề | lấy đúng 5 màu này cho màu trong hình |
| `balloon` | vật duy nhất mang màu rực | hình không thêm vật đỏ thứ hai ngoài khi nó là chủ đề |
| `tape`, `splat` | băng giấy, bắn mảng màu | lặp lại ở góc tờ giấy trong hình cho đồng bộ |

## 4. Bốn công thức (khung 1920x1080)
**a. Bìa:** chữ bìa nằm trái (x 120 đến 1020). Hình đặt trong x 1120 đến 1820, y 200 đến 740: một **tờ sổ ký họa dán băng giấy hai góc**, bên trong một vật lặp hai lần (bản mờ nét đứt, bản đậm có màu lệch) nối bằng vòng cuốn gió và nhãn viết tay; bút mực nằm vắt góc dưới, vệt màu tràn ra ngoài mép tờ. Dải nhà phố của diễn viên `row` nằm ngay dưới (y từ 700), diễn viên `sky` là tờ nền; hình có giấy trắng làm "vầng sáng" nên không rối với nét nhà phía sau.

**b. Sơ đồ khái niệm (3 đến 5 thành phần):** hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980), trên nền vệt trời của diễn viên `sky` (tư thế slide chẵn). **Chừa dải y 590 đến 670** cho `hl-text`. Nửa trên (y 280 đến 560): cảnh nhỏ có một vật ở hai tư thế A, B, đường đi chấm, ba vòng số. Nửa dưới (y 690 đến 980): bảng ghi chú viết tay, mỗi dòng một vòng số, nhãn ngắn, một ký hiệu màu nhỏ bên phải, gạch chân đứt.

**c. Quy trình hoặc dòng thời gian:** diễn viên `ground` đã là trục mực ở y 630; đặt SVG chồng lên (left 120, top 560, cao 140). Trạm ở x = 136 + i x 342,4 (5 bước), mỗi trạm một **vết màu lệch + vòng mực**, màu lấy theo bộ swatch (trời, lá, đá, mái, đèn); cung nối mực giữa hai trạm cao tối đa 38px phía trên trục, mũi tên đặc; trạm cuối thêm vòng thứ hai. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh:** trên `stats`, dải đáy y 840 đến 970. Mỗi cột một **trang nhỏ** (210x104) có băng giấy ở góc, nền màu lệch cùng màu với số (hồng đất, lá, trời), bên trong các vạch mực mô phỏng dòng chữ nhiều dần và mảnh dần (3, 5, 7). Tâm cột: x 384, 960, 1536. Cột cuối thêm vết cắt đứt giữa trang và hai mũi tên tách ra. So sánh hai phương án: hai trang cạnh nhau cùng tỷ lệ.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: nét liền thêm `class="draw" pathLength="1"` và `style="--d:.3"`, cần `morph-motion.css`. Thứ tự đúng với ký họa: **mực trước** (khung, nét nhà), rồi màu hiện sau bằng `<g class="reveal">`, rồi chữ viết tay. Không gắn `draw` vào nét đứt (`us-g`, `us-d`) vì `draw` ghi đè `stroke-dasharray`.
- Cả hình xong trong khoảng 2 giây. Không dùng animation lặp, không rung, không đổi màu. Màu không "bật": hiện dần bằng `reveal`.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"`, `width`, `height` thì xuất thành hình vector, hiện bằng hiệu ứng quét nếu bên trong có `draw`. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.us-k`), nên đặt tên lớp riêng có tiền tố `us-`. Bộ lọc màu nước có thể không hiển thị trong PowerPoint (màu phẳng hơn, vẫn đẹp).
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn viết tay rất ngắn; câu cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không đè dải `hl-text`.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`.
- Rà màu: chỉ dùng bảng màu ở mục 2; mực luôn là `var(--ink)`.

## 6. Cấm
- Mực đổi màu hoặc đen tuyền; viền màu liền khít với nét mực (mất cảm giác lệch lớp); tô kín mép giấy sát khung (phải chừa lề và để mép loang).
- Render 3D, bóng đổ cứng, glow, gradient rực; màu rực ngoài bóng bay đỏ.
- Hình đè lên chữ, nét chạy qua hàng tiêu đề, chữ dài trong SVG.
- Số đo, số liệu bịa trong hình; địa danh hoặc biển hiệu thật, logo thật, chữ ký người thật.
- Vẽ người có mặt; nếu cần dáng người chỉ dùng "người que" rất nhỏ (đầu chấm, hai nét chân), mặt để trống.
- Phần chỉ dành cho video (camera, âm thanh, nhân vật cử động liên tục, hình "sôi" 12 khung mỗi giây) không áp dụng cho slide.

Phỏng theo lemo-opuscar `styles/urban-sketch/STYLE.md` (MIT) qua MotionFly.
