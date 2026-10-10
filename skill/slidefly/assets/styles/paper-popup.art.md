# Sách pop-up giấy: luật vẽ minh họa SVG cho từng slide

Dùng cùng `paper-popup.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một tấm thẻ giấy mới bật lên từ trang sách. Deck mẫu: `gallery/81_demo-paper-popup.html`.

## 1. Tinh thần
- Cả deck là **một cuốn sách pop-up mở trên bàn**: trang kem có nếp gấp giữa, tấm bìa dựng đứng làm phông, mọi vật là **thẻ giấy phẳng cắt rời** đặt trên trang và dựng lên quanh mép đáy.
- **Mọi mảnh giấy có cùng một cách làm:** bóng đổ theo đúng hình cắt, mép bìa cứng màu be xám lệch xuống 3px, viền trắng ngà dày 13px, mảng màu phẳng bão hòa kiểu sách thiếu nhi (không neon), nét mực nâu sẫm 3,4px. Một lát liềm tối (hard crescent) thay cho đổ bóng mềm.
- **Không có gì tròn xoe kiểu 3D**: chỉ gấp, cong, trượt. Vật "3D" là vài thẻ phẳng chồng nhau. Mặt xoay là lật ngang, không xoay quanh trục đứng.
- Hai thế giới: **trang sách thật** (ấm, tự nhiên) và **thế giới giấy** (rực). Hình vẽ luôn thuộc thế giới giấy, đứng trên trang.
- Giọng điệu: kể chuyện, vui, nhẹ. Mặt chỉ vài nét (hai chấm mắt, một nét cười, má hồng). Vật là mặt trời trên cán, cây, nấm, hoa, hàng rào, thẻ kéo.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực | #4A2E1B (không bao giờ đen tuyền) |
| Viền giấy, mép bìa | #FFF8EA, #CDB98F |
| Trời, cỏ nhạt, cỏ | #8CCBEA, #A8D56B, #6DB655, lá #4FA94A |
| Vàng, cam, đỏ | #FFC93C, #F59E0B, #D9382B; đỏ san hô cho nhãn #FF7A59 |
| Tím, xanh dương, xanh ngọc | #A35BD6, #2F6FB8, #2FB3A3, xanh lá nhãn #2A8C4F |

- **Lớp thẻ** theo thứ tự vẽ (mỗi mảnh làm đủ 4 lớp rồi mới sang mảnh sau; mảnh ghép nhiều hình cùng một thẻ thì vẽ viền và mép cho cả nhóm trước, mực sau cùng để các nét giao nhau bên trong biến mất):
  1. bóng `#3C2810` alpha .16, lệch (8, 12);
  2. mép bìa `#CDB98F`, stroke `border + 3`, lệch xuống 3px;
  3. viền `#FFF8EA`, stroke 13px, `stroke-linejoin: round`;
  4. màu phẳng + nét mực (hoặc nét mực dày gấp đôi bên dưới rồi tô màu đè lên cho nhóm hợp nhất).
- Khai báo các lớp `.pp-k .pp-t .pp-g .pp-d .pp-ar .pp-lb .pp-num` trong `<style>` của deck (xem deck mẫu) để bản PPTX đọc được màu và nét.
- Chữ: `var(--font-display)` (Baloo 2, 800) cho nhãn, số trắng trong huy hiệu tròn; 24 đến 34px, chỉ nhãn ngắn.

## 3. Hình mẫu lặp lại
**Mặt trời trên cán** (12 cánh tròn, đĩa vàng, mặt cười):
```svg
<path d="M110 36a19 19 0 1 0 .1 0Z" fill="#F59E0B" stroke="#4A2E1B" stroke-width="3"/>
<circle cx="110" cy="104" r="56" fill="#FFC93C" stroke="#4A2E1B" stroke-width="3"/><circle cx="96" cy="100" r="4.6" fill="#4A2E1B"/><circle cx="124" cy="100" r="4.6" fill="#4A2E1B"/>
```
**Huy hiệu số** (tròn, màu theo cột, số trắng):
```svg
<circle cx="48" cy="466" r="20" fill="#FF7A59" stroke="#4A2E1B" stroke-width="3"/><text class="pp-num" x="48" y="476" text-anchor="middle">1</text>
```
**Thanh giấy ghi chú** (nhãn): hình chữ nhật bo góc trắng có viền ngà, bóng nhẹ, huy hiệu số bên trái, chữ Baloo 30px, ký hiệu nhỏ bên phải.
**Thẻ kéo (pull-tab):** một cửa sổ cắt trên thẻ, dải giấy chạy phía sau, đầu dải thò ra mép phải có núm tròn đỏ san hô và hai mũi tên.
**Vật hai tư thế:** tư thế cũ nét đứt không màu, tư thế mới đầy đủ, đường đi bằng chấm, mũi tên đặc.
**Chân gấp chữ V:** hai hình bình hành be nhạt dưới thẻ, một đường gấp dọc giữa, nét mực mảnh: nói "thẻ này bật lên từ trang".
**Mảnh giấy màu** (confetti): hình chữ nhật, tam giác, tròn xoay ngẫu nhiên, viền trắng ngà, bóng lệch 4px; dùng ở góc để nối hình với lề.

## Diễn viên của style và vai của chúng quanh minh họa
| Diễn viên | Vai | Gợi ý khi vẽ hình |
|---|---|---|
| `board` | tấm bìa dựng làm phông, đổi màu theo trang (trời, hồng, chàm đêm, vàng bơ, cam hoàng hôn) | hình đặt lên phông, không tô phông thứ hai |
| `cloud`, `sun` | mây, mặt trời trên cán | một mặt trời mỗi hình là đủ, tư thế A, B vẽ lại cùng dáng |
| `hill1`, `hill2`, `fence` | hai lớp đồi cắt, hàng rào (thành trục thời gian ở slide `timeline`) | hình đứng trên đồi, đáy thẻ ngang mép đồi |
| `tree`, `mush`, `flower` | cây, nhà nấm, hoa | không vẽ lại; lấy làm bảng màu |
| `scrap` | mảnh giấy màu vãi ở góc | lặp lại vài mảnh quanh hình cho đồng bộ |
| `crease` | nếp gấp giữa sách | chữ và hình chạm nếp gấp vẫn phải đủ tương phản |

## 4. Bốn công thức (khung 1920x1080)
**a. Bìa:** chữ bìa nằm trái trên trang trái (x 120 đến 940). Hình đặt trong x 1240 đến 1740, y 150 đến 670: một **thẻ pull-tab** đứng trên chân gấp chữ V, cửa sổ chứa cảnh nhỏ (đồi, mặt trời tư thế A, bóng ma tư thế B), núm kéo thò ra mép phải, chú thích một dòng bên dưới. Phông xanh trời, nấm, cây, hàng rào, hoa do diễn viên dựng quanh.

**b. Sơ đồ khái niệm (3 đến 5 thành phần):** hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980). **Chừa dải y 590 đến 670** cho `hl-text`. Nửa trên: một thẻ cảnh nhỏ có đồi, một vật hai tư thế A, B, đường chấm, ba huy hiệu số. Nửa dưới (y 440 đến 700): ba thanh giấy ghi chú, mỗi thanh một huy hiệu số cùng màu với huy hiệu trên cảnh.

**c. Quy trình hoặc dòng thời gian:** diễn viên `fence` là trục ở y 630; đặt SVG chồng lên (left 120, top 560, cao 140). Trạm ở x = 136 + i x 342,4 (5 bước), mỗi trạm một **hình dán** khác dáng (tròn, vuông bo, tam giác, sao, tim) khác màu; cung nối cao tối đa 44px phía trên trục, mũi tên đặc. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh:** trên `stats`, dải đáy y 840 đến 970. Mỗi cột một **thẻ đứng** (210x104) trên chân gấp, bên trong 3, 5, 7 thanh giấy màu mảnh dần theo màu số (san hô, xanh lá, xanh dương). Tâm cột: x 384, 960, 1536. Cột cuối thêm vết cắt đứt và hai mũi tên tách ra.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: nét liền thêm `class="draw" pathLength="1"` và `style="--d:.3"`, cần `morph-motion.css`. Thứ tự: thẻ bật lên bằng `<g class="reveal">` (từ dưới trang lên), rồi đường đi, rồi nhãn. Không gắn `draw` vào nét đứt (`pp-g`, `pp-d`).
- Cả hình xong trong khoảng 2 giây. Không animation lặp, không rung. Giấy cứng: chuyển động có điểm dừng, không co giãn như đất sét.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"`, `width`, `height` thì xuất thành hình vector. Diễn viên được xuất riêng, tên `!!` để Morph (cây, nấm, mặt trời mọc lên hoặc gập xuống nhờ đổi chiều cao). Chữ trong SVG không sửa được trong PowerPoint: chỉ để nhãn ngắn.
- `clipPath` trong hình dùng id riêng (`ppA1w`); mọi SVG chung một tài liệu nên id không được trùng.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không đè dải `hl-text`.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`; chữ đỏ nhấn trên nền kem đạt tương phản 4,5:1.

## 6. Cấm
- Màu neon, gradient mượt, bóng mềm kiểu 3D, glow, phối cảnh hội tụ; viền đen; mực đen tuyền.
- Hình tròn xoe có chiều sâu, đổ bóng tròn: mọi vật phải là thẻ phẳng.
- Hình đè lên chữ, nét chạy qua hàng tiêu đề, chữ dài trong SVG.
- Nhân vật, logo, giao diện của game hoặc sách có thật; chữ Hán giả; số đo bịa.
- Phần chỉ dành cho video (camera macro, HDRI, độ sâu trường ảnh, âm thanh giấy, nhân vật bước đi liên tục) không áp dụng cho slide.

Phỏng theo lemo-opuscar `styles/paper-popup/STYLE.md` (MIT) qua MotionFly.
