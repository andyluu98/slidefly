# Đèn lồng giấy: luật vẽ minh họa SVG cho từng slide

Dùng cùng `den-long-giay.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một tấm bìa cắt đặt trong hộp đèn. Deck mẫu: `gallery/82_demo-den-long-giay.html`.

## 1. Tinh thần
- Cả deck là **một hộp đèn giấy cắt trong đêm Trung thu**: các lớp bìa xếp chồng, ánh sáng ấm chỉ lọt qua những chỗ đã cắt thủng. Hình trong minh họa cũng là bìa cắt, không phải nét vẽ mực.
- **Ngôn ngữ cắt giấy**: hình khối phẳng một màu, mép gọn, chi tiết bằng lỗ cắt (thoi, giọt, tròn nhỏ, vòng chấm), không viền đậm, không đổ bóng mềm.
- **Thang giá trị tạo chiều sâu**: lớp xa sáng và lạnh (mây xanh tím, trăng kem), lớp gần tối gần như đen, ánh sáng ấm chỉ nằm trong đèn và ô cửa.
- Nhân vật là vật và con vật của lễ hội (đèn ông sao, đèn tròn, thỏ ngọc, mái phố cổ, mây cuộn). Không vẽ người, không vẽ khuôn mặt tả thực.
- Một màu nhấn duy nhất: hổ phách ấm. Đỏ chỉ dùng cho tua rua, nến và chấm mũi.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Giấy sáng (thỏ, thẻ) | `#f6e2b0`, thẻ giấy `#f7d98c` |
| Thân đèn | `var(--lamp)` (#ff9a3a), viền `#8f2417` mờ 60% |
| Ánh sáng qua lỗ cắt | `#fff2c4` (lớp `dl-cut`), hổ phách `var(--amber)` |
| Tua, nến | `var(--lamp-red)` (#d6401f) |
| Bìa tối | `var(--night)` (#0b1232), nắp đèn `#3a1410`, vàng đồng `#e8b941` |
| Dây treo | `#d8b45e`, dày 3px |
| Chữ nhãn | `var(--cream)`, `var(--font-body)` 600, in hoa, giãn 0,12em, 17 đến 22px |

- Hai độ dày nét: dây và nét chính 3px, nét phụ 2px. `stroke-linecap` và `stroke-linejoin` để `round`.
- Nét đứt `9 8` dành cho tư thế cũ hoặc "bóng ma" của vật; nét liền cho tư thế mới.
- **Ánh sáng** vẽ bằng `radialGradient` hổ phách từ 55% về 0 (id riêng cho mỗi SVG, ví dụ `dlH1`), đặt sau thân đèn. Không dùng `filter`, không `mix-blend-mode`.
- **Thứ tự lớp trong một hình:** hào quang, dây, thân đèn, lỗ cắt, nắp và tua, rồi mới đến nhãn.
- Khai báo lớp (`.dl-paper .dl-lamp .dl-cut .dl-hole .dl-night .dl-cord .dl-line .dl-ghost .dl-ink .dl-ar .dl-tag .dl-bead .dl-lb .dl-num`) trong `<style>` của deck (xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Bộ hình mẫu lặp lại
**Đèn tròn** (thân elip, gân dọc, lỗ thoi, nắp, tua):
```svg
<ellipse class="dl-lamp" cx="410" cy="216" rx="50" ry="54"/>
<path d="M410 172V260M380 178Q364 216 380 254M440 178Q456 216 440 254" fill="none" stroke="#7a1d10" stroke-opacity=".42" stroke-width="2"/>
<path class="dl-cut" d="M410 190l9 14l-9 14l-9 -14z"/>
<rect x="396" y="160" width="28" height="12" rx="4" fill="#3a1410"/>
```
**Dây treo kèm hạt số** (hạt tròn có chữ A, B hoặc số, giống thẻ đố đèn):
```svg
<path class="dl-cord" d="M410 74V164"/>
<circle class="dl-bead" cx="410" cy="116" r="17"/><text class="dl-num" x="410" y="124" text-anchor="middle">B</text>
```
**Đèn ma** (tư thế cũ): cùng hình đèn nhưng lớp `dl-ghost` (nét đứt hổ phách, không tô). **Cung chuyển** nối tư thế cũ sang mới: `<path class="dl-ghost" d="M180 154C240 118 320 130 356 196"/>` kèm mũi tên đặc `dl-ar` đặt đúng hướng tiếp tuyến cuối cung.
**Thẻ giấy** (hình chữ nhật `dl-tag`, lỗ xỏ dây là chấm tối, biểu tượng nét `dl-ink` nâu `#5a2a10`) treo dưới dây bằng một đoạn `dl-cord`, nhãn chữ ngay dưới thẻ.
**Hào quang:** `<circle cx="410" cy="218" r="90" fill="url(#dlH2)"/>`.
**Đường chấm tách đôi** (nét đứt dọc giữa đèn, hai mũi tên đặc hướng ra hai bên) nói "tách", "chia ra".

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ nằm trái (x 120 đến 1040); trăng, đèn tròn, đèn ông sao, đèn trụ và đám mây do diễn viên của style đã dựng ở nửa phải. Hình riêng đặt lên **đám mây dưới trăng** (khoảng x 1150 đến 1425, y 500 đến 740): một con vật kể chuyện lễ hội, tô giấy sáng `#f6e2b0` để nổi trên nền đêm. Deck mẫu: thỏ ngọc ngồi trên mây, giơ cao một chiếc đèn nhỏ về phía trăng.
- Lớp vẽ: hào quang đèn nhỏ, dây và đèn nhỏ, tai, thân, đuôi, chân, đầu; hoa văn cắt hổ phách trên thân.
- Tai và thân là hai hình riêng để lỗ cắt tách rõ; mắt là chấm tối, mũi chấm đỏ.
- Không đặt hình chồng lên đuôi đèn ông sao (cuối y 450) và tua đèn tròn (x 1520 đến 1640).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 270 đến 990). Chừa dải y 600 đến 660 cho `hl-text`. Nửa trên: một sợi dây ngang, một vật ở hai tư thế (đèn ma nét đứt và đèn sáng có hào quang, độ dài dây là tư thế), cung chuyển có mũi tên, hạt chữ A và B. Nửa dưới: một sợi dây thứ hai treo ba thẻ giấy đánh số 1, 2, 3, mỗi thẻ một biểu tượng nét (đèn thoi, mũi tên lên xuống, cung trượt) và nhãn ngắn dưới thẻ.
- Cao nhất của đèn chính không quá y 300 của SVG để không chạm dải hl-text.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; diễn viên `garland` đã là sợi dây có đèn nhỏ và các chấm trạm nằm đúng trên dây (x = 131 + i × 342,4 với 5 bước). Hình riêng thể hiện **ánh sáng tăng dần**: mỗi trạm i có quầng sáng bán kính 20 + 5,5i và i cung tròn đồng tâm phía trên trục, nối các trạm bằng cung hổ phách cao tối đa 30px kèm mũi tên.
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674); cung đồng tâm lớn nhất bán kính 43.

**d. Con số hoặc so sánh.** Trên `stats`, dải đáy y 836 đến 986 dưới mỗi con số: mỗi cột một chiếc đèn tròn nhỏ, **số lỗ cắt bằng số ý** (3, 5, 7 lỗ thoi, nhỏ dần). Cột "nên tách slide" thêm đường đứt dọc giữa đèn và hai mũi tên ra hai bên. Tâm cột x 384, 960, 1536 (số trong SVG: 264, 840, 1416 khi SVG đặt ở left 120). So sánh hai phương án: hai đèn cạnh nhau cùng cỡ, khác số lỗ.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.2"`, cần `morph-motion.css`. Dùng cho dây và cung chuyển. Không gắn `draw` vào nét đứt (`draw` ghi đè `stroke-dasharray`).
- Đèn, hạt, thẻ và hào quang: bọc `<g class="reveal">` hoặc thêm `reveal` để hiện sau nét. Nhịp: dây `--d:.2`, đèn sau đó, cung nối trễ thêm 0,2 giây mỗi cung; cả hình xong trong khoảng 2 giây.
- Không animation lặp, không nhấp nháy, không đổi màu. Ánh sáng nhấp nháy đã dành cho các diễn viên.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.dl-lamp`), nên dùng lớp có tiền tố `dl-`. Gradient đặt bằng thuộc tính `fill="url(#id)"`.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn (A, B, số, một đến hai từ). Câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không đè lên đèn hay tua của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ dùng các màu của bảng ở mục 2. Đèn phải sáng hơn nền xung quanh, lớp xa sáng hơn lớp gần.
- Thử đếm: hình bìa có đúng một con vật, hình sơ đồ có đúng ba thành phần, hình quy trình có đúng số trạm của slide.

## 6. Cấm
- Màu ngoài bảng: xanh lá, tím rực, trắng lạnh; gradient màu ngoài hào quang hổ phách; bóng đổ mềm, glow neon, render 3D.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Hình thật có bản quyền: đèn của một thương hiệu, nhân vật hoạt hình, logo, chữ Hán làm họa tiết khi không hiểu nghĩa.
- Ghi số đo, số liệu bịa vào hình: dùng chữ ký hiệu (A, B, 1, 2, 3) hoặc số đúng như nội dung slide.
- Đặt đèn sáng lên nền sáng (đèn mất chiều sâu); đưa lớp gần sáng hơn lớp xa.
- Vẽ người hay mặt người chi tiết; câu dài trong SVG.

Phỏng theo lemo-opuscar `styles/paper-lantern/STYLE.md` (MIT) qua MotionFly.
