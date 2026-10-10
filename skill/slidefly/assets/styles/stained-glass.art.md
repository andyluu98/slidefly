# Kính màu: luật vẽ minh họa SVG cho từng slide

Dùng cùng `stained-glass.css`. Lớp sân khấu đã dựng sẵn gian đá tối, cửa sổ nhọn (lancet), cửa sổ hoa hồng, thanh sắt ngang, dải viền ngọc trai, tia sáng và vệt màu rơi xuống nền. File này dạy vẽ **một minh họa SVG inline riêng cho mỗi slide**, như một ô kính nữa được ghép vào cùng cửa sổ. Deck mẫu: `gallery/74_demo-stained-glass.html`.

## 1. Tinh thần
- **Những mảnh kính màu cắt tay, ghép bằng thanh chì đen dày.** Mỗi mảnh một màu phẳng, viền chì bo tròn; chi tiết (nếp, hoa văn) vẽ bằng nét nâu mảnh gọi là grisaille. Không vẽ hình có viền đen mảnh kiểu vector, không kaleidoscope.
- **Kính không tự phát sáng.** Nó chỉ rực khi có nắng sau lưng: ô kính trong minh họa là phần sáng nhất slide; nền đá và ô kính mờ (độ mờ thấp) là phần tối. Tránh màu nhạt phấn: màu đậm, bão hòa, như ngọc.
- **Hai màu gánh bức tranh** (xanh cobalt sâu và đỏ rubi), ba bốn màu khác chỉ là điểm nhấn nhỏ (vàng, lục, tím mận). Vàng dành cho mặt trời, ánh sáng và chữ mạ vàng.
- **Thế tục.** Hoa hồng, thoi (lozenge), ngọc trai, mặt trời, lá. Không thập tự, thánh, vòng hào quang hay biểu tượng tôn giáo.
- Kính không uốn, không mờ dần: vật hiện ra bằng cách được chiếu sáng, thành từng mảnh cứng. Khác `art-deco` (kim loại, đối xứng hình học, nền đen vàng phẳng): ở đây là chì, kính, ánh sáng xuyên và nền đá.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Lớp CSS trong deck | Giá trị |
|---|---|---|
| Cobalt (nền kính) | `sg-cb`, `sg-cb2` | #2457B5, #3470D6 |
| Rubi | `sg-rb` | #B3182C |
| Vàng, vàng sáng | `sg-gd`, `sg-gd2` | #E6AE2E, #F6CC5A |
| Lục | `sg-gr` | #2F8A55 |
| Tím mận | `sg-mu` | #8A2F68 |
| Kính trắng xanh | `sg-wh` | #D6E8D0 |
| Giấy da (băng chữ) | `sg-par` | #EBDDB5 |
| Chì | viền của mọi lớp `sg-*` | #0F0B09, nét 6px (4px mảnh `sg-t`, 3,5px nhỏ `sg-x`) |
| Grisaille | `sg-gris` | #3A2210 độ mờ 62% |
| Mạ vàng trên nền tối | `sg-gild`, `sg-gildS`, `sg-lb` | #F0C25E |

- Mỗi mảnh = một lớp `sg-*` (đã có viền chì). Tô màu bằng **class trong khối `<style>` của deck**, không ghi `fill="var(...)"`; PPTX chỉ đọc màu từ class (thuộc tính `fill="#..."` trực tiếp thì được).
- **Mọi mảnh có chi tiết:** một nét sáng "cạo kính" `sg-hi` (trắng, độ mờ 55%) ven mảnh, hoặc vài nét grisaille xiên (nếp, bóng). Mảnh phẳng trơn trông như clip-art.
- **Chì chỉ nằm nơi hai màu gặp nhau.** Cùng một màu thì cùng một mảnh, không chia nhỏ.
- **Mảnh cắt có góc, không có góc lõm sâu;** đường cong mềm (Catmull-Rom hoặc Bezier), hình thoi, vòng tròn, cung.
- **Sáng nền đá và chữ:** chữ mạ vàng `var(--gold)` hoặc giấy da `var(--parch)` trên nền tối; trong băng chữ giấy da thì chữ nâu đen #2B1D10. Chữ tiếng Việt dùng `var(--font-display)` (Cormorant Garamond 700, IN HOA, giãn 0,1em), 22 đến 26px.
- Mọi `id` (clipPath) phải duy nhất trong cả deck: `sgc1`, `sgs1`.

## 3. Hình mẫu lặp lại
**Đĩa mặt trời kính** (vàng, mười tia xen vàng sáng và đỏ, lõi trắng; dùng cho "một vật", nút quy trình, đích đến):
```svg
<path class="sg-rb sg-t" d="M88 74L112 56L98 78Z"/>   <!-- một tia -->
<circle class="sg-gd" cx="88" cy="100" r="32"/><circle class="sg-gd2 sg-t" cx="88" cy="100" r="19"/><circle class="sg-wh sg-x" cx="88" cy="100" r="8"/>
```
**Trạm tròn** (đĩa đá tối r 33 che thanh sắt, đĩa kính r 26, lõi vàng, nét sáng):
```svg
<circle cx="136" cy="70" r="33" fill="#2A221B"/><circle class="sg-cb2" cx="136" cy="70" r="26"/>
<circle class="sg-gd2 sg-x" cx="136" cy="70" r="9"/><path class="sg-hi" d="M119 66A18 18 0 0 1 130 54"/>
```
**Ô kính vòm nhọn** (cắt bằng `clipPath`, các dải kính chồng nhau, viền rubi, chì ngoài):
```svg
<clipPath id="sgs1"><path d="M207 144V74C207 40 238 12 264 -4C290 12 321 40 321 74V144Z"/></clipPath>
<g clip-path="url(#sgs1)"><rect class="sg-cb2" .../><rect class="sg-gd2" .../><path d="..." fill="none" stroke="#B3182C" stroke-width="22"/></g>
<path d="..." fill="none" stroke="#0F0B09" stroke-width="9"/>
```
**Băng chữ giấy da** (nhãn ngắn: hai đầu cắt chéo, chữ nâu đen): `<path class="sg-par sg-x" d="..."/><text class="sg-ink" text-anchor="middle">TƯ THẾ A</text>`.
**Dây mạ vàng** nối hai vật: `<path class="sg-gild" d="M146 90C196 54 246 42 288 56"/>` (nét đứt 12 9) kèm đầu mũi tên là một mảnh `sg-gd2`.
**Vết nứt** (ánh sáng chạy qua mảnh vỡ): đường gãy khúc `sg-crack` (kem sáng 4px) đặt trên `sg-crackG` (vàng mờ 11px).
**Số trong đĩa vàng** để nối hình với bảng kê: `<circle class="sg-gd2 sg-x" r="19"/><text class="sg-num" text-anchor="middle">1</text>`.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa bên trái (x 120 đến 1040). Cửa sổ của style chiếm x 1140 đến 1780, y 4 đến 930 (hai lancet dưới một hoa hồng), thanh sắt ngang y 560 đến 576. SVG đặt `left:1320px; top:500px; width:280; height:280`: **một đĩa huy chương ghim vắt qua hai lancet**, tâm (1460, 640), đè lên thanh sắt. Vành rubi có 16 ngọc trai vàng, nền trong là trời cobalt, dải vàng sáng ở chân trời, đồi lục; vật chính của chủ đề (deck mẫu: máy bay giấy cho "slide biết bay") làm từ ba mảnh kính trắng, cobalt đậm, rubi cùng nét grisaille.
- Không vẽ ra ngoài đường kính 252px quanh tâm; không đè lên chữ.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content` là ô kính mờ (độ mờ 34%) cao tới y 1030. SVG đặt `left:1290px; top:400px; width:480; height:560`, **mở đầu bằng một tấm bảng tối** (`rect` #140F0B độ mờ 80%, viền vàng mảnh) để chữ đọc rõ trên ô kính đằng sau, rồi vẽ kính sáng lên trên. Chừa dải **y 590 đến 672** (tọa độ cục bộ 190 đến 272) cho `hl-text`. Nửa trên: một vật, hai tư thế (đĩa mặt trời kính nhỏ và lớn, dây mạ vàng nối, băng chữ giấy da dưới mỗi đĩa, cùng đĩa số 1). Nửa dưới: bảng kê gồm các hàng đĩa số, mảnh kính màu, vạch giả chữ.
- Một thành phần = một vật hoặc một tư thế; cùng một vật thì cùng số.

**c. Quy trình hoặc dòng thời gian.** Thanh sắt `saddle` là trục (y 623 đến 639). SVG đặt chồng lên trục y 630 của `timeline`: `left:120px; top:560px; width:1680; height:140`. Mỗi bước một **trạm tròn** tại x = 16 + i × 342,4 (5 bước), y cục bộ 70, màu kính lần lượt cobalt, rubi, lục, tím mận; trạm cuối là **đĩa mặt trời** vì đó là nơi ánh sáng tới. Giữa hai trạm là cung dây mạ vàng cao tối đa 30px kèm một chiếc lá lục. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải y 836 đến 986 dưới mỗi con số: `left:120px; top:836px; width:1680; height:150`, tâm cột cục bộ x 264, 840, 1416. Mỗi cột một ô kính vòm nhọn rộng 116, cao 138, ghép từ **số dải kính bằng số ý** (3, 5, 7): nhiều ý thì dải mỏng đi. Cột "nên tách slide" có vết nứt sáng chạy dọc ô kính. So sánh hai phương án: hai ô kính cạnh nhau, một sáng một mờ.

## 5. Chuyển động và xuất PPTX
- Mảnh hiện bằng cách **được chiếu sáng**: bọc `<g class="reveal">` (hiện dần, trượt nhẹ), từng nhóm một: vành, nền, vật chính, nét grisaille, nhãn. Không xoay, không uốn, không mờ nhòe.
- Không dùng animation lặp, không đổi màu, không rung lắc. Cả hình xong trong khoảng 2 giây. Có thể gắn `draw pathLength="1"` cho nét liền dài (không gắn vào `sg-gild` vì `draw` ghi đè nét đứt).
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng thuộc tính `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.sg-cb`). SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG là một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn trong SVG, câu chữ cần sửa để ngoài SVG.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: kính sáng nằm trên nền tối hoặc trên tấm bảng tối, nét không chạm chữ, không vào hàng tiêu đề, không lệch khỏi trục và cửa sổ của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ cobalt, rubi, vàng, lục, tím mận, trắng xanh và chì; không gradient trong mảnh kính, không biểu tượng tôn giáo.
- Rà chữ: chữ vàng hoặc giấy da trên nền tối, chữ nâu đen trong băng giấy da; mọi `id` duy nhất.

## 6. Cấm
- Thập tự, thánh, hào quang, mọi biểu tượng tôn giáo. Gạch khảm (mosaic) phản chiếu; kính không có độ cong 3D.
- Gradient trong mảnh kính (mỗi mảnh một màu phẳng), bóng đổ mềm, glow neon, viền đen mảnh quanh hình.
- Màu nhạt phấn. Quá hai màu chủ đạo cùng lúc trên một hình.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165, vào dải `hl-text` (y 590 đến 672 của slide `content`) hoặc trục timeline.
- Ghi số liệu bịa trong hình (số dải kính chỉ minh họa "càng nhiều ý càng mỏng"); dùng chữ ký hiệu hoặc nhãn "VÍ DỤ". Chữ dài trong SVG; người vẽ thay cho vật.

Phỏng theo lemo-opuscar `styles/stained-glass/STYLE.md` (MIT) qua MotionFly.
