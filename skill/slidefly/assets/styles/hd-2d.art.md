# HD-2D: luật vẽ minh họa SVG cho từng slide

Dùng cùng `hd-2d.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một khung hình trong một mô hình thu nhỏ có đèn. Deck mẫu: `gallery/87_demo-hd-2d.html`.

## 1. Tinh thần
- Cả deck là **một diorama thu nhỏ về đêm**: nhân vật pixel phẳng, thấp độ phân giải, đứng trong một thế giới có lớp, có sương, có đèn. Cái chuyển động mượt là ánh sáng và lớp nền, không phải nhân vật.
- **Ánh sáng là chủ thể.** Một tông nền lạnh lớn (chàm, tím, xanh đêm) đối lập với vài nguồn sáng ấm nhỏ (đèn lồng, ô cửa sổ, đèn đường) mang câu chuyện. Hình nào cũng có một nguồn sáng thấy được và một vũng sáng trên mặt đất.
- **Hai mức độ nét**: sprite và đồ vật nền vẽ bằng ô pixel vuông, góc cạnh. Vầng sáng, bóng và sương vẽ bằng hình tròn, elip trong suốt, mềm. Đừng trộn nét mềm vào sprite.
- Nhìn từ trên xuống và hơi xéo: đáy của vật chuẩn là một mặt phẳng nghiêng, các sprite đứng thẳng như tấm bìa cắt (billboard). Không nhìn ngang tầm mắt.
- Một kim loại duy nhất cho khung giao diện: **vàng**, trên một tấm tối trong mờ. Nhân vật chính mặc **màu đỏ san hô**, màu mà không bối cảnh nào dùng.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực, tối nhất (không dùng đen thuần) | #14102e |
| Tấm giao diện | #0e0a24 mờ 80 đến 85 phần trăm, viền vàng #e8c27a |
| Nền lạnh (sương mỗi slide) | #2b2a66, #1e2554, #4a2c66, #1d2f5c, #322868, #3a2148 |
| Đá, sàn | #4a3f78, sáng #5a4e90, tối #2b2554, khe #221d48 |
| Đèn ấm | #ffb347, lõi #fff3c4, vàng đồng #e8c27a |
| Nhân vật chính | áo #e8553a, bóng áo #b13e2e, da #f2c9a0 |
| Chữ | kem #f6ecd6 |

- **Ô pixel 4, 6 hoặc 8 đơn vị**, bọc bằng `shape-rendering="crispEdges"`. Sprite viết thành lưới chữ rồi đối xứng nửa trái sang nửa phải để chắc cân xứng:
```
....kk   ...khh   ..khhh   ..khss   ..ksks   ..kccc   .kcccy   .kccCC   (nửa trái 12 x 16 của người lữ hành)
```
- **Vầng sáng** là các vòng tròn đồng tâm cùng màu ấm, độ mờ 0,07 đến 0,2, lõi nhỏ đậm nhất. Không `filter`, không gradient trong SVG ở hình lớn (bản PPTX giữ vòng tròn tốt hơn):
```svg
<circle cx="350" cy="250" r="150" fill="#ffb347" fill-opacity=".07"/><circle cx="350" cy="250" r="108" fill="#ffb347" fill-opacity=".09"/>
<circle cx="350" cy="250" r="72" fill="#ffb347" fill-opacity=".12"/><circle cx="350" cy="250" r="39" fill="#ffb347" fill-opacity=".2"/>
```
- **Bóng** là elip #05030f mờ 0,4 đặt lệch **ra xa** nguồn sáng. **Vũng sáng** là elip ấm mờ 0,2 và 0,28 chồng nhau trên mặt đất.
- Mặt phẳng nghiêng (đế diorama) vẽ bằng ba đa giác: mặt trên, mặt trái đậm hơn, mặt phải đậm nhất; khe lát đá là các đường song song hai trục, mờ 0,7.
- Chữ: nhãn tên hình bằng `var(--font-display)` (Cormorant 700, IN HOA, giãn 0,2em, vàng), chữ thường bằng `var(--font-body)` (Cormorant Garamond 600). Khai báo lớp `.hd-t .hd-b .hd-n .hd-m` trong `<style>` của deck để bản PPTX đọc được.

## 3. Hình mẫu lặp lại
Mọi hình mẫu dưới đây dùng đúng bảng màu ở mục 2 và lặp lại giữa các slide của cùng một deck.
**Đèn lồng giấy tượng trưng cho một slide:** hình chữ nhật bo góc kem, viền vàng 4px, hai vạch chữ giả, bao ba vòng sáng. Nghiêng nhẹ 5 đến 8 độ, lơ lửng.
**Căn nhà pixel:** thân kem, mái đỏ nâu bậc thang, cửa gỗ, một ô cửa sổ sáng có vầng tròn.
**Cây thông pixel:** hai ba tầng chữ nhật xanh đậm có viền sáng trên cùng, thân nâu hai ô.
**Đèn đường:** sprite 10 x 22 (đầu đèn vàng, lõi sáng, cột tối) kèm vầng sáng bốn vòng.
**Bảng kê (hộp thoại):** tấm tối viền vàng 3px, đường viền mảnh vàng mờ bên trong, **bảng tên** nằm đè lên mép trên, mỗi hàng một viên thoi vàng chứa số, tên mục bên trái, ghi chú nghiêng bên phải.
**Viên thoi số:** hình thoi mực viền vàng 3px, số kem bên trong; cùng một vật thì cùng số.
**Tia lấp lánh:** chữ thập 6 x 6 kem mờ 0,85, hai cánh mờ 0,5. Rải bảy đến mười tia quanh nguồn sáng và đèn lồng, không rải khắp hình.
**Hạt sáng (số ý):** vòng tròn ấm có ba lớp (vầng ngoài 2,3 lần bán kính, vầng trong 1,5 lần, lõi đặc) và một điểm kem lệch trên trái.
**Khung vàng trong hình:** hình chữ nhật bo góc 6, viền vàng 3px, thêm một viền mảnh 1,5px vàng mờ 0,45 thụt vào 8px, nền #0e0a24 mờ 85 phần trăm.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa trong khung vàng bên trái (x 80 đến 1080). Hình đặt trong x 1120 đến 1820, y 200 đến 740: **một đảo diorama lơ lửng** (đế xéo, cả hai mặt bên) giữa các cột sáng, trên mặt có nhà, thông, đèn mặt đất, và phía trên là ba đèn lồng giấy là các slide. Nhân vật chính và đèn đường lớn đứng dưới đất do hai diễn viên `hero`, `lamp` dựng, không vẽ lại trong hình.
- Lớp vẽ: nhãn "HÌNH 1 · DIORAMA", bóng đảo, đế, vũng sáng, bóng, nhà, đèn, thông, đèn lồng giấy, tia lấp lánh.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Gọn trong khung vàng của diễn viên `panel` (x 1240 đến 1820, y 250 đến 1010). Chừa dải y 600 đến 660 cho `hl-text` (SVG y 320 đến 380). Nửa trên: **cùng một sprite ở hai trạng thái ánh sáng**: tư thế A lạnh và tối (phủ một lớp xanh #0a1040 mờ 0,42) trên bệ tím, tư thế B được đèn chiếu ấm có vầng sáng, nối bằng cung nét chấm vàng có mũi tên. Nửa dưới: bảng kê có bảng tên "BẢNG KÊ" và ba hàng.

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`. Diễn viên `floor` (y 612 đến 656) là con đường lát đá. Mỗi bước một **đèn lồng sáng** (đầu đèn của sprite đèn, 40 x 32px) đặt giữa đường ở x = 136 + i × 342,4, có vầng sáng bán kính 56px; đèn cuối to hơn (60 x 48px, vầng 82px) và sáng nhất. Giữa các đèn là các chấm vàng nhỏ so le như dấu chân. Không vẽ nét vào vùng chữ (trên y 586, dưới y 674); vầng sáng chỉ là vòng mờ 0,07 đến 0,2 nên chữ vẫn đọc rõ. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986: mỗi cột một khung vàng (260 x 108) chứa đúng bấy nhiêu hạt sáng ấm bằng số ý (3 to, 5 vừa, 7 nhỏ, vầng sáng nhỏ dần). Cột "nên tách slide" thêm biển cảnh báo hình thoi viền san hô. Tâm cột: x 384, 960, 1536.

## 5. Chuyển động và xuất PPTX
- Hiện theo nhịp nhẹ: `<g class="reveal-scale">` cho sprite, đèn, bảng; `reveal` cho nhãn. Thêm `style="--i:n"` để so le. Trong `<style>` của deck đặt `.art .reveal-scale { transform-box: fill-box; transform-origin: 50% 80%; }`.
- Không đặt `transform` trên chính phần tử có lớp `reveal*` (CSS sẽ ghi đè thuộc tính `transform`): bọc thêm một `<g>` ngoài, `transform` đặt ở `<g>` trong.
- Thứ tự hiện gợi ý: đế và bóng trước, sprite và đồ vật sau, vầng sáng cuối cùng, để người xem thấy như đèn vừa được bật.
- Mỗi hình dùng tối đa ba nhóm `reveal`, nhóm sau trễ `--i` thêm 1; cả hình xong trong khoảng 2 giây.
- Không animation lặp, không nhấp nháy: lửa đèn chỉ sáng đều. Sprite đứng yên, ánh sáng đổi theo từng slide qua diễn viên.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. Chỉ dùng `<rect>`, `<circle>`, `<ellipse>`, `<path>`, `<polygon>`, `<text>`, `<g>`. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165; vầng sáng không làm chữ khó đọc.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: chỉ dùng bảng ở mục 2; mọi sprite có viền #14102e.

## 6. Cấm
- Bloom thật, làm mờ (`filter`), gradient mịn trên sprite, chữ nghiêng có nét lạ cho đoạn dài.
- Nhân vật hay đồ vật có dáng cuốn tròn mềm (sprite phải là lưới ô vuông); nhân vật cao hơn 1/8 chiều cao khung hình.
- Tên, nhân vật, địa danh, hoa văn khung, giai điệu, logo của trò chơi HD-2D có thật; không nhắc tên chúng trong hình.
- Vẽ cảnh ban ngày không đèn trong cùng deck (trừ khi nội dung đòi hỏi); số liệu bịa trong hạt sáng: số hạt chỉ thể hiện đúng số ý.
- Đè hình lên chữ của slide; câu dài trong SVG.
- Dùng nhiều hơn hai nguồn sáng ấm trong cùng một hình: ánh sáng phải dẫn mắt về một chỗ.
- Màu san hô của nhân vật chính xuất hiện ở bất kỳ vật nào khác ngoài nhân vật đó.

Phỏng theo lemo-opuscar `styles/hd-2d/STYLE.md` (MIT) qua MotionFly.
