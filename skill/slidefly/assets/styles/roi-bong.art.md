# Múa rối bóng: luật vẽ minh họa SVG cho từng slide

Dùng cùng `roi-bong.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một con rối da được cắt thêm cho buổi diễn. Deck mẫu: `gallery/83_demo-roi-bong.html`.

## 1. Tinh thần
- Cả deck là **một tấm màn vải sáng cam, đèn dầu đặt sau**: hình là da thuộc đã cắt, gần như đen, ánh đèn xuyên qua những chỗ đục thủng. Chỗ nào đục thì thấy màn vải, chỗ nào chồng lên nhau thì tối hơn.
- **Ngôn ngữ cắt chạm**: bóng đen đặc có viền gọn, chi tiết hoàn toàn bằng lỗ (vảy hình trăng khuyết, lưới thoi, đồng tiền lỗ vuông, xoắn ốc mây, lá, khe mảnh). Không tô gradient, không đổ bóng.
- **Màu là thuốc nhuộm trong suốt**: chỉ vài mảng nhỏ (tay áo, lông chim, mái ngói, mặt trời) nhuộm son hoặc vàng nghệ; mọi đường nét và khớp là da đen.
- Chuyển động của rối là xoay quanh **đinh khớp** và trượt theo **que điều khiển**, không bao giờ biến dạng. Hình tĩnh trong minh họa vẫn phải đọc ra "vật này gắn khớp ở đâu, que nằm ở đâu".
- Nhân vật là rối cổ trang, chim hạc, mây, tòa đình, cây thông; không vẽ người thật, không logo.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Da đen (bóng, viền, khớp) | `var(--ink)` (#26110a), lớp `rb-ink` |
| Thuốc nhuộm son | `#c4341a`, lớp `rb-red` |
| Thuốc nhuộm vàng nghệ | `#e0a52a`, lớp `rb-och` |
| Mặt vải sáng (đồng tiền, số) | `#ffe9a8`, lớp `rb-cloth` |
| Dây, que điều khiển | nét `var(--ink)` 3 đến 4px, lớp `rb-cord` |
| Nét phụ, mũi tên | `rb-line` 3,2px, `rb-ar` đặc; tư thế cũ nét đứt `9 8` (`rb-ghost`) |
| Chữ nhãn | `var(--font-body)` 700, in hoa, giãn 0,12em, 18 đến 20px; số trong đồng tiền `var(--font-display)` 800 |

- **Lỗ là lỗ thật:** vẽ một hình bằng một `<path fill-rule="evenodd">` gộp viền ngoài và các lỗ, để màn vải (và diễn viên phía sau) lộ ra qua lỗ. Không vẽ lỗ bằng ô màu sáng chồng lên.
- Chỉ dùng các màu trong bảng. Không `filter`, không `mix-blend-mode`; chồng lớp thuốc nhuộm thì dùng `fill-opacity`.
- Khai báo lớp (`.rb-ink .rb-red .rb-och .rb-cloth .rb-cord .rb-line .rb-ghost .rb-ar .rb-ring .rb-lb .rb-num`) trong `<style>` của deck để bản PPTX đọc được màu và nét.

## 3. Bộ hình mẫu lặp lại
**Vảy giáp** (hàng hình trăng khuyết so le, mỗi hàng lệch nửa bước): trăng khuyết là hình tròn bán kính 10 trừ một hình tròn nhỏ hơn đẩy lên 3,8px. **Lưới thoi** (hình thoi 22x28 so le) cho áo choàng và ống chân. **Đồng tiền** (lỗ tròn có hình vuông da còn lại ở giữa) cho đai, bệ và dải phân cách. **Xoắn mây** (đường xoắn ốc 2 vòng, dày 6 đến 7px) cho mây và cổ áo. **Lá** (lá nhọn dài 22, rộng 7) rải trong tán thông.
**Đinh khớp** (vòng da, vòng sáng, nút tối ở tâm):
```svg
<path class="rb-ink" fill-rule="evenodd" d="M165 150a15 15 0 1 0 -30 0a15 15 0 1 0 30 0zM159 150a9 9 0 1 1 -18 0a9 9 0 1 1 18 0zM154 150a4 4 0 1 0 -8 0a4 4 0 1 0 8 0z"/>
```
**Tay áo nhuộm son** (ống thon, vài lỗ tròn dọc thân) gắn vào thân bằng đinh khớp; bàn tay là hình tròn da đen đặc.
**Biển da** (bảng kể chuyện): hình chữ nhật da đen, một khung hẹp chạm thủng sát mép, nội dung là khe cắt. Treo bằng hai sợi `rb-cord`.
**Biển da với chữ là khe cắt** (một path `evenodd`: viền ngoài, khung chạm thủng, rồi từng khe là một hình chữ nhật bo tròn):
```svg
<path class="rb-ink" fill-rule="evenodd" d="M164 26H364V138H164ZM172 34V130H356V34ZM176 38H352V126H176Z M204 62h144v8h-144z M204 82h120v8h-120z M204 102h132v8h-132z"/>
<path class="rb-cord" d="M194 0V26M334 0V26"/>
```
Số khe bằng số ý của cột; chiều dài mỗi khe lệch nhau 20 đến 40px cho giống dòng chữ thật.
**Que điều khiển:** một nét thẳng `rb-cord` (4px) đi từ bàn tay hoặc cổ xuống mép dưới của hình, kèm tay cầm bằng một nét ngang ngắn.
**Đồng tiền số** (tag chú thích): `<circle class="rb-cloth" r="17"/>` kèm `rb-ring` và chữ số `rb-num`, nối với vật bằng nét `rb-line` 2px.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ nằm trái (x 120 đến 1040); rối tướng, mặt trời, hạc, mây, cây thông và dải đất chạm thủng do diễn viên của style dựng ở nửa phải. Hình riêng thêm **một thứ mang nghĩa "slide"**: một biển da mang cảnh nhỏ (mặt trời nhuộm vàng nghệ, núi chạm vảy, chim) treo bằng hai sợi dây từ chân con hạc, tua son phía dưới (deck mẫu: khung khoảng x 1066 đến 1266, y 396 đến 509, xoay -6 độ).
- SVG phủ cả khung 1920x1080 để dây có thể bám theo chân hạc; dây hội tụ tại một nút ngay dưới chân hạc.
- Không đè lên chữ tiêu đề (x lớn nhất khoảng 1020).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 270 đến 990). Chừa dải y 600 đến 660 cho `hl-text`. Nửa trên: thân rối có vảy giáp, một cánh tay nhuộm son quay quanh đinh khớp (tư thế cũ nét đứt, tư thế mới đặc), cung xoay có mũi tên đặt đúng hướng tiếp tuyến, que điều khiển rũ xuống từ bàn tay, một đèn dầu nhỏ có tia sáng, ba đồng tiền số 1, 2, 3 nối vào khớp, que, đèn. Nửa dưới: sợi dây treo ba biển da vuông, mỗi biển một biểu tượng đục thủng (vòng khớp, que có tay cầm, ngọn lửa trên đĩa đèn) và nhãn ngắn dưới biển.
- Phần đồ họa nửa trên không vượt y 300 của SVG.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`; diễn viên `strip` (dải đồng tiền) chính là trục, các chấm trạm là đồng tiền sáng nằm trên dải (x = 131 + i × 342,4 với 5 bước). Hình riêng cho **thuốc nhuộm ngấm dần**: mỗi trạm một đĩa son trong suốt, độ đậm tăng 0,22 đến 0,9, viền ring mảnh, nối các trạm bằng cung mực có mũi tên cao tối đa 40px.
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên `stats`, dải đáy y 836 đến 986: mỗi cột một **biển da** treo hai dây, chữ là các khe cắt: 3 khe dày, 5 khe vừa, 7 khe mảnh. Biển cột "nên tách slide" xẻ làm hai nửa, dịch ra hai bên, kèm đường đứt dọc giữa và hai mũi tên. Tâm cột x 384, 960, 1536 (trong SVG đặt ở left 120 là 264, 840, 1416).

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.2"`, cần `morph-motion.css`. Dùng cho que điều khiển, cung nối. Với cung vốn nét liền, thêm `stroke-dasharray:none` trong `style` để tránh `draw` ghi đè.
- Biển, đồng tiền, nhãn: bọc `<g class="reveal">` cho hiện sau nét. Cả hình xong trong khoảng 2 giây.
- Không animation lặp, không rung. Sự "run tay" của rối chỉ nằm ở diễn viên, không thêm vào minh họa.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.rb-ink`), nên dùng lớp có tiền tố `rb-`. Hình có lỗ phải là một path `evenodd`.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn (số, một đến hai từ).

## Thứ tự lớp trong một hình
1. Hào quang hoặc đĩa nhuộm trong suốt nằm dưới cùng.
2. Dây, que (nét mảnh) rồi mới đến thân da đen, để dây luồn ra sau mảnh.
3. Mảnh nhuộm son hoặc vàng nghệ chồng lên da (tay áo, lông chim, mái ngói).
4. Đinh khớp và đồng tiền số nằm trên cùng, kèm nhãn chữ.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không chạm chân hay que của rối diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc các path có lỗ sang được PowerPoint.
- Rà màu: chỉ da đen, son, vàng nghệ và mặt vải sáng. Mọi bóng đen phải có ít nhất một khe hoặc lỗ để đọc ra là da chạm.

## 6. Cấm
- Màu ngoài bảng (xanh lam, tím, hồng), gradient, bóng đổ mềm, glow, ánh kim; hình khối 3D hay cảnh nhìn xa gần.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Vẽ lỗ bằng ô màu sáng chồng lên da (lỗ phải thật); viền dày đều kiểu hoạt hình cắt giấy.
- Ghi số đo, số liệu bịa vào hình; chữ Hán hay chữ giả làm họa tiết.
- Sao chép một con rối, bản nhạc, kịch bản có thật; nhân vật có bản quyền.
- Biến dạng, bóp méo, uốn cong một mảnh da: mảnh chỉ xoay, trượt hoặc thay thế.

Phỏng theo lemo-opuscar `styles/shadow-puppet/STYLE.md` (MIT) qua MotionFly.
