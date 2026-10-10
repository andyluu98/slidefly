# Phim câm: luật vẽ minh họa SVG cho từng slide

Dùng cùng `silent-film.css`. Lớp sân khấu đã dựng sẵn rạp chiếu: màn nhung, tấm thẻ chữ đen viền trang trí, mặt phim màu sepia bạc có vệt xước và bụi, cuộn phim và dải phim có lỗ răng cưa. File này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, như một khung hình của cùng cuốn phim. Deck mẫu: `gallery/75_demo-silent-film.html`.

## 1. Tinh thần
- **Một bản in mực và lớp màu nước xám**, chiếu trên phim bạc: nét khắc, nhiều bậc xám, gạch bóng 45 độ ở vùng tối. Không phải ảnh chụp phủ bộ lọc sepia, không phải hoạt hình hiện đại.
- **Không ai nói.** Người đóng vai bằng dáng điệu trong khung cảnh rộng; chữ thuộc về thẻ chữ đen (intertitle) hoặc nhãn ngắn. Cảnh quay "đóng đinh": một khung rộng nhìn cả nguyên nhân lẫn hậu quả.
- **Diễn kiểu điềm tĩnh:** mặt gần như không đổi (hai nét mắt, một nét miệng), cơ thể làm việc; nhân vật nhận ra qua dáng (mũ, áo, đồ vật), không cần chân dung kỹ.
- **Một sắc bạc, không màu.** Giá trị sáng tối gánh cả bức tranh (nền sáng với áo tối, mặt sáng trên nền tối). Màu duy nhất được thêm là đỏ nâu đậm (oxblood) ở chữ số, và vàng hổ phách trên thẻ đen.
- Rạp luôn hiện diện: màn nhung hai bên, mép phim cháy sẫm, vết xước và bụi, lỗ răng cưa của dải phim. Khác `vintage-editorial` (giấy báo ấm, bố cục tạp chí, không có rạp và phim).

## 2. Bảng màu, nét, chất liệu
| Vai trò | Lớp CSS trong deck | Giá trị |
|---|---|---|
| Năm bậc xám (sáng tới tối) | `sf-f1` đến `sf-f7` | #E4DAC0, #C9BB98, #A8977A, #8F7A57, #6E5E46, #4A3C2C, #2E241A |
| Mực | `sf-ink`, nét `sf-l` | #1E1610, nét 2,5px |
| Giấy phim, nền trời | `sf-sep`, `sf-pale` | #DACEB2, #F2EBDA |
| Nét kem trên nền đen | `sf-lC`, `sf-lCT`, `sf-bar` | #EFE4C8 |
| Dải phim đen | `sf-film`, `sf-frame`, `sf-frameD` | #17110C |
| Băng dính nối phim | `sf-tape` | #EFE4C8 độ mờ 92% |
| Đỏ nâu (chữ số, hiếm) | trong CSS style: `var(--ox)` | #8F2A1A |

- Tô màu bằng **class trong khối `<style>` của deck**, không ghi `fill="var(...)"`; PPTX chỉ đọc màu từ class (thuộc tính `fill="#..."` trực tiếp và `fill="url(#id)"` cho gạch bóng thì được).
- **Gạch bóng 45 độ** bằng `<pattern patternTransform="rotate(45)">` khoảng 6px, nét 1,5px mực, phủ lên vùng tối ở độ mờ 35 đến 55%. Vùng sáng không gạch.
- **Nền tối lùi, nền sáng tiến:** xa thì nhạt (xám 1 đến 3), gần thì đậm (xám 5 đến 7); chiều sâu bằng giá trị, không bằng mờ nhòe.
- **Vật là hình khối phẳng + gạch bóng**, nét viền chỉ ở vật chính (tay nhân vật, máy bay giấy, mép chữ nhật). Nhân vật: mũ lưỡi trai, mặt sáng, áo khoác tối, chân thẳng.
- **Khung phim:** hình chữ nhật đen, hàng lỗ răng cưa (12x8, bo 2) ở trên và dưới, cửa sổ ảnh ở giữa. Vẽ bằng hàm lặp, không tay từng lỗ.
- **Chữ trong hình:** tiếng Việt dùng `var(--font-display)` (Playfair Display SC 700), 21 đến 25px, kem trên nền đen; số lùn trong vòng tròn nét kem.
- Mọi `id` (clipPath, pattern) phải duy nhất trong cả deck: `sfc`, `sfh1`, `sft0`.

## 3. Hình mẫu lặp lại
**Khung phim** (đen, hàng lỗ trên dưới, cửa sổ ảnh bên trong):
```svg
<rect class="sf-frame" x="2" y="54" width="238" height="140"/>
<rect class="sf-cream" x="14" y="59" width="12" height="8" rx="2"/>  <!-- lặp 8 lỗ trên, 8 lỗ dưới -->
<rect class="sf-win" x="16" y="76" width="210" height="96"/>
```
**Vật có gạch bóng** (đĩa tối, gạch phủ, một nét sáng cạo bóng):
```svg
<circle class="sf-f7" cx="62" cy="148" r="17"/><circle cx="62" cy="148" r="17" fill="url(#sfh2)" fill-opacity=".5"/>
<path class="sf-lC" style="stroke-width:2" d="M52 145A10 10 0 0 1 56 138"/>
```
**Đường bay in từng chấm** (vật vừa ném, vết đi): `<path class="sf-trail" d="M70 334C110 270 190 196 280 148"/>` (nét 2,6px, `stroke-dasharray: 2 9`, đầu tròn). **Nét tốc độ**: ba nét ngắn song song sau vật.
**Băng dính nối phim** (dấu "cắt, tách"): hình thang kem đè lên khung, hai nét ngắn trên dưới, một nét đứt dọc giữa.
**Cung chữ số** (nối hình với bảng kê): `<circle ... fill="none" stroke="#EFE4C8" stroke-width="3"/><text class="sf-num">1</text>`.
**Bảng kê kiểu cue sheet:** mỗi hàng: vòng số, khung phim nhỏ có ô xám, hai vạch giả chữ `sf-bar`.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Thẻ chữ đen chiếm khung 4:3 giữa hai tấm màn (x 240 đến 1680); chữ bìa nằm bên trái (x 340 đến 960). Diễn viên `iris` là **đĩa ảnh** tâm (1330, 540), đường kính 560, viền cháy sẫm. SVG đặt `left:1070px; top:280px; width:520; height:520`, **cắt bằng `clipPath` hình tròn r 250 quanh tâm (260, 260)**: một cảnh quay rộng: trời nhiều bậc xám, mây, nhà xa, nhà gần có gạch bóng, mái nhà có người đội mũ lưỡi trai vừa ném một vật (deck mẫu: máy bay giấy cho "slide biết bay"), đường chấm bay lên, vài nét tốc độ.
- Lớp vẽ: trời, mây, hàng nhà xa kèm cửa sổ, nhà giữa, nhà gần, mái, nhân vật, đường bay, vật bay. Không vẽ ra ngoài đĩa; chữ không nằm trong ảnh.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content` là **tấm thẻ đen** (viền kép, bốn góc quạt) x 1240 đến 1840, y 230 (hoặc 250) đến 1010. SVG đặt `left:1262px; top:336px; width:556; height:640`, vẽ nét kem và xám sáng trên nền đen. Chừa dải **y 590 đến 672** (tọa độ cục bộ 254 đến 336) cho `hl-text`. Nửa trên: hai khung phim cạnh nhau, cùng một vật ở hai tư thế (nhỏ, thấp bên trái; to, cao bên phải), mũi tên đứt giữa hai khung, nhãn "TƯ THẾ A/B" dưới mỗi khung. Nửa dưới: bảng kê gồm các hàng vòng số, khung phim nhỏ với ô xám, vạch giả chữ.
- Một thành phần = một vật hoặc một tư thế; cùng một vật thì cùng số.

**c. Quy trình hoặc dòng thời gian.** Diễn viên `strip` là trục (dải phim y 598 đến 662, x 120 đến 1800, lỗ răng cưa hai hàng). SVG đặt chồng lên trục y 630 của `timeline`: `left:120px; top:560px; width:1680; height:140`. Mỗi bước một **khung phim** rộng 108, cao 60 tại x = 16 + i × 342,4 (5 bước), y cục bộ 40 đến 100, ảnh nhỏ bên trong là cùng một cảnh với **mặt trời lên cao dần** qua từng khung (cảnh đầu bị đồi che nửa); khung cuối có tia. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải y 836 đến 986 dưới mỗi con số: `left:120px; top:836px; width:1680; height:150`, tâm cột cục bộ x 264, 840, 1416. Mỗi cột một khung phim 240x134 có **số dải xám bằng số ý** (3, 5, 7): nhiều ý thì dải mỏng đi, độ xám chuyển từ sáng sang tối. Cột "nên tách slide" thêm băng dính nối phim chạy dọc khung. So sánh hai phương án: hai khung phim cạnh nhau, cùng cỡ, cùng bậc xám.

**e. Đĩa ảnh cho section, quote, closing.** Cùng cách với bìa: SVG `aria-hidden` đặt đúng tâm đĩa `iris` rồi `clipPath` tròn nhỏ hơn đĩa 10 đến 30px để lộ viền cháy.
- `section`: đĩa đường kính 640, tâm (1360, 550); `left:1080px; top:270px; width:560; height:560`. Đề xuất vật làm phim: máy quay quay tay trên chân ba càng, hai hộp phim, tay quay, vệt sáng chiếu chéo.
- `quote`: đĩa nhỏ 140 như lỗ nhòm, tâm (960, 130); `left:890px; top:60px; width:140; height:140`. Một vật đơn độc (đèn đường có chùm sáng), nền xám đậm.
- `closing`: đĩa 280 phía trên chữ, tâm (960, 220); `left:820px; top:80px; width:280; height:280`. Cú ném mũ lên không trung kèm vệt chấm và vài nét tia, mặt đất tối ở đáy.
- Mỗi đĩa chỉ một vật chính, có gạch bóng ở phần tối; không để nét chạm vòng viền cháy.

## 5. Chuyển động và xuất PPTX
- Mỗi khung phim hiện bằng một nhịp: bọc `<g class="reveal">` (hiện dần, trượt nhẹ), lần lượt từng khung rồi nhãn. Không xoay, không phóng; đây là máy quay nặng, cảnh đứng yên.
- Không dùng animation lặp, không đổi màu, không rung lắc (vệt xước và bụi đã nằm trong lớp sân khấu). Có thể gắn `draw pathLength="1"` cho nét liền; không gắn vào `sf-trail` hay `sf-lD` vì `draw` ghi đè nét đứt.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng thuộc tính `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.sf-f3`). SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn trong SVG, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không lệch khỏi đĩa ảnh, thẻ đen và dải phim của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ năm bậc xám bạc, mực, kem trên nền đen; không gradient màu, không màu rực.
- Rà hình: người nhỏ trong cảnh rộng, không giống Charlot; mọi `id` duy nhất.

## 6. Cấm
- Màu rực, gradient màu, bóng đổ màu, glow neon, render 3D. Nhiều hơn một sắc ngoài bạc (đỏ nâu chữ số và vàng hổ phách trên thẻ đen đã là đủ).
- Chân dung cận cảnh lớn (nhìn như ma-nơ-canh): giữ người nhỏ trong cảnh rộng hoặc trong đĩa ảnh.
- Giống Charlot (mũ phớt tròn, ria bàn chải, gậy, dáng đi vịt), nhân vật hoặc cảnh phim có thật, tên rạp, logo hãng phim thật.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165, vào dải `hl-text` (y 590 đến 672 của slide `content`) hoặc trục timeline.
- Ghi số liệu bịa trong hình (số dải xám chỉ minh họa "càng nhiều ý càng mỏng"); dùng chữ ký hiệu hoặc nhãn "VÍ DỤ". Chữ dài trong SVG.

Phỏng theo lemo-opuscar `styles/silent-film/STYLE.md` (MIT) qua MotionFly.
