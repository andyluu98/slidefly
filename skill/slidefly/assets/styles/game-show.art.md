# Game show: luật vẽ minh họa SVG cho từng slide

Dùng cùng `game-show.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một tấm "cảnh quay" của chương trình. Deck mẫu: `gallery/85_demo-game-show.html`.

## 1. Tinh thần
- Cả deck là **một trường quay truyền hình vui nhộn, vẽ phẳng**: màu kẹo, nét mực dày, bóng đổ cứng lệch xuống góc phải dưới. Mỗi slide là một "vòng chơi" đổi tông màu nền.
- **Nhân vật là đồ chơi.** Một kiểu thân duy nhất cho cả dàn: thân đậu tròn, tay cụt có găng, mắt bầu dục có đốm sáng, miệng mở khi hô. Phân biệt bằng màu thân, mảng bụng kem và một phụ kiện trên đầu (ăng ten, tim, chồm tóc).
- **Mỗi cảnh một câu chuyện nhỏ**: một lời hô (nhãn "TUYỆT!"), một lượt đáp, một bảng điểm. Không đoạn văn trong hình.
- Chỉ nét phẳng: không gradient, không mờ, không chất liệu giấy. Chiều sâu chỉ đến từ bóng đổ cứng.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực (viền, bóng cứng) | `var(--ink)` #1B1035 |
| Giấy, nền thẻ | `var(--cream)` #FFF3D6 |
| Vàng, cam, đỏ | #FFD23F, #FF9A3C, #FF4F5E |
| Hồng, xanh lá, chanh | #FF7EB6, #2EC27E, #B5E04A |
| Trời, xanh dương, tím | #4CC9F0, #3A6BFF, #5B3FC4 |

- Viền mực 8px cho nhân vật và vật lớn, 5 đến 7px cho chi tiết nhỏ, `stroke-linejoin` và `stroke-linecap` để `round`.
- **Bóng đổ cứng:** vẽ lại đúng hình đó bằng màu mực, dịch (8, 8) cho nhãn và bảng, rồi mới vẽ hình màu lên trên. Không dùng `filter`, không `opacity` cho bóng.
- Một vòng một màu: nền slide đã đổi theo `game-show.css`, nhân vật không được trùng màu với nền nó đứng (bảng nền: tím, xanh dương, vàng, xanh lục, hồng, cam, xanh navy, xanh trời, đỏ).
- Chữ trong hình: `var(--font-display)` (Baloo 2 800), IN HOA, nhãn ngắn 20 đến 40px, màu mực hoặc kem. Khai báo lớp trong `<style>` của deck (`.gs-w .gs-sm .gs-l .gs-n`) để bản PPTX đọc được.

## 3. Hình mẫu lặp lại
**Nhân vật đậu** (chân ở y = 0, gốc đặt ở bàn chân giữa):
```svg
<g transform="translate(150 650) scale(.74)" stroke-linejoin="round" stroke-linecap="round">
  <path d="M-58 -10C-58 -94 -34 -132 0 -132C34 -132 58 -94 58 -10Q58 3 46 3H-46Q-58 3 -58 -10Z" fill="#4CC9F0" stroke="#1B1035" stroke-width="8"/>
  <ellipse cx="0" cy="-34" rx="32" ry="28" fill="#FFF3D6"/>   <!-- bụng -->
  <ellipse cx="-21" cy="-86" rx="10" ry="15" fill="#1B1035"/> <!-- mắt, thêm đốm sáng trắng r4 -->
</g>
```
Tay giơ lên hoặc buông xuống: vẽ bằng hai nét chồng (mực 26px rồi màu thân 11px) để có viền mà không cần thêm hình.
**Nhãn phán quyết** (sao nhiều cánh có bóng cứng, vòng hồng đứt nét, chữ nghiêng 10 độ): `TUYỆT!`, `ĐÚNG!`, `HAY!`.
**Bảng điểm** (thẻ kem bo góc, bóng cứng, dải đỏ tiêu đề, các hàng thanh màu bo tròn):
```svg
<rect x="28" y="418" width="500" height="252" rx="26" fill="#1B1035"/>
<rect x="20" y="410" width="500" height="252" rx="26" fill="#FFF3D6" stroke="#1B1035" stroke-width="7"/>
```
**Bóng đèn** (vòng tròn vàng, viền mực 4px, đốm trắng nhỏ lệch trên trái) dùng cho điểm, trạm, vạch đếm.
**Confetti** (tròn, tam giác, vuông xoay, sóng) rải thưa, viền mực 5px, không chạm chữ.
**Phụ kiện đầu** để nhận ra từng nhân vật, mỗi nhân vật đúng một món:
- ăng ten: que mực 6px, bi vàng viền mực 5px;
- tim: que ngắn, hình tim đỏ viền mực 5px;
- chồm tóc: hình ba múi vàng viền mực 6px đặt lên đỉnh thân.
**Vật thể ẩn dụ** (tấm slide, thẻ, bảng) thành đồ chơi bằng cách thêm mắt, miệng, tay và chân vào đúng hình khối của nó, giữ viền 8px và bóng cứng.
**Cung nhảy** nối hai trạng thái: nét chấm tròn đầu (`stroke-dasharray: 4 14`, `stroke-linecap: round`) kết thúc bằng mũi tên đặc xoay theo tiếp tuyến.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa bên trái (x 120 đến 1040). Hình đặt trong x 1120 đến 1820, y 200 đến 930, **đứng trên bục** do diễn viên `podium` đã dựng (bục 1 có mặt trên ở y 780, tâm x 1470; bục 2 y 850, tâm x 1270; bục 3 y 910, tâm x 1670). Trong hệ tọa độ SVG (gốc 1120, 200): chân nhân vật chính ở (350, 580), hai đối thủ nhỏ (tỷ lệ .74) ở (150, 650) và (550, 710).
- Nhân vật chính là **vật của chủ đề** hóa thành đồ chơi (deck mẫu: tấm slide có mặt, tay, chân, ăng ten), hai tay giơ lên, nhãn "TUYỆT!" phía trên phải, sao 4 cánh và confetti xung quanh.
- Lớp vẽ: đối thủ, nhân vật chính, nhãn, sao. Mỗi cụm bọc `<g class="reveal-scale">` để bật lên lần lượt.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Gói trong thẻ kem của diễn viên `card` (x 1240 đến 1820, y 250 đến 1010). Chừa dải y 600 đến 660 cho `hl-text` (SVG y 320 đến 380). Nửa trên: nhân vật cùng một màu ở hai tư thế (tay buông, tay giơ), nối bằng cung nhảy nét chấm có mũi tên, mỗi nhân vật một bóng số (cùng vật thì cùng số). Nửa dưới: bảng kê (cột SỐ, TÊN, GHI CHÚ) có thanh màu.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; diễn viên `marquee` đã là dải đèn làm trục (y 608 đến 652). Mỗi bước một "trạm" (vòng tròn màu có ký hiệu, bóng đổ cứng) ở x = 136 + i × 342,4 (5 bước), cung nhảy nối hai trạm cao tối đa 46px trên trục, mũi tên quay theo tiếp tuyến. Trạm cuối là sao phán quyết có dấu tích. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ vào vùng chữ (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986: mỗi cột một bảng đèn (thẻ kem, bóng cứng) có số bóng bằng đúng ý của số (deck mẫu: 3, 5, 7 bóng, bóng nhỏ dần; cột "nên tách slide" thêm nút X đỏ). Tâm cột: x 384, 960, 1536. So sánh hai phương án: hai bảng cùng cỡ, bên thắng có sao.

## 5. Chuyển động và xuất PPTX
- Hiện theo nhịp "bật": `<g class="reveal-scale">` cho nhân vật, nhãn, bảng; `reveal` cho nhãn chữ. Thêm `style="--i:n"` để so le. Trong `<style>` của deck đặt `.art .reveal-scale { transform-box: fill-box; transform-origin: 50% 80%; }` để bật quanh tâm hình.
- Cung nhảy trên trục thêm `class="draw" pathLength="1"` và `--d` tăng dần 0,2 giây mỗi cung. Không gắn `draw` vào nét chấm (nó ghi đè `stroke-dasharray`).
- **Không** đặt `transform` trên chính phần tử có lớp `reveal*` (CSS sẽ ghi đè thuộc tính `transform`): bọc thêm một `<g>` ngoài cho lớp hiệu ứng.
- Không animation lặp, không rung lắc: nhịp nhảy của nhân vật nằm ở cách chuyển slide, không ở hình.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.gs-w`); màu viền và tô viết thẳng thành thuộc tính `fill`, `stroke`.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`. Chữ trong SVG không sửa được trong PowerPoint: chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, chân nhân vật đứng đúng mặt bục.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ dùng bảng màu ở mục 2; mọi nét viền là mực.

## 6. Cấm
- Gradient, bóng mờ, `filter`, chất liệu giấy, 3D, hiệu ứng phát sáng.
- Hai nhân vật cùng màu với nền chỗ đứng, hay màu thân đổi giữa các hình của cùng một deck.
- Số điểm, số liệu bịa: dùng số bóng đèn, thanh dài ngắn hoặc chữ ký hiệu (A, B, 1, 2, 3 chỉ thứ tự).
- Tên, nhân vật, giao diện, âm nhạc của trò chơi nhịp điệu hay chương trình có thật; logo thật.
- Đè hình lên chữ của slide; câu dài trong SVG; nhân vật người thật.

Phỏng theo lemo-opuscar `styles/game-show/STYLE.md` (MIT) qua MotionFly.
