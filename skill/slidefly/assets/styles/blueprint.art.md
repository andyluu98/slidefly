# Blueprint: luật vẽ minh họa SVG cho từng slide

Dùng cùng `blueprint.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một "HÌNH n" trên cùng một tờ bản vẽ. Deck mẫu: `gallery/58_demo-blueprint.html`.

## 1. Tinh thần
- Cả deck là **một tờ giấy cyanotype xanh Phổ**: nét trắng kỹ thuật vẽ theo đúng thứ tự của người kỹ sư, khô và chính xác; phần ghi chú mới được phép dí dỏm hay ấm áp.
- **Ngôn ngữ nét 2D**: hình chiếu thẳng góc, mặt cắt, hình chiếu xiên bằng nét. Không render 3D.
- **Quy ước mang giọng điệu**: đường tâm, đường bao, gạch mặt cắt, đường kích thước, bóng số, khung tên. Nhân vật là vật được thiết kế (máy, chi tiết, công trình), không vẽ người.
- **Chỉ xanh và trắng.** Trắng đổi độ dày và độ mờ, không đổi sắc. Một màu ngoài xanh dùng đúng một lần trong deck: con dấu đỏ (đã có sẵn ở slide closing của style), mang phán quyết.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Nét chính | `var(--line)` (#e7f0f9) |
| Nét phụ, đường kích thước | `var(--line-soft)` (trắng 62%) |
| Nét mảnh, gạch mặt cắt | `var(--hair)` (trắng 30%) |
| Tô "giấy" dưới đường bao | `var(--fill)` (#22488f) |
| Vùng xanh đậm (vết nước) | `var(--deep)` (#0f2350) |
| Con dấu (cấm dùng trong minh họa) | `var(--stamp)` |

- Bốn độ dày trên khung 1920x1080: đường bao 4px, chi tiết 2,5px, mảnh và kích thước 2px, gạch mặt cắt 1,2px. `stroke-linecap` và `stroke-linejoin` để `round`.
- Kiểu nét: đường tâm `stroke-dasharray: 22 6 4 6`; nét khuất `10 7`; đường cắt, đường di chuyển (phantom) `28 6 6 6 6 6`.
- **Luật che khuất theo thứ tự vẽ:** vật đặc tô `fill: var(--fill)` rồi mới vẽ viền, để che nét phía sau.
- Gạch mặt cắt 45 độ bằng `<pattern patternTransform="rotate(45)">`, khoảng cách 10 đến 14px.
- Chữ: tiếng Việt dùng `var(--font-display)` (Barlow Condensed 600, IN HOA, giãn 0,06em); số, mã, ký hiệu Latin dùng `var(--font-mono)` (JetBrains Mono). Nhãn 19 đến 24px.
- Khai báo lớp nét trong `<style>` của deck (`.bp-o .bp-d .bp-t .bp-hid .bp-cl .bp-ph .bp-ar .bp-bal .bp-lb .bp-mono`, xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Hình mẫu lặp lại
**Bóng số** (vòng tròn có số, kèm đường dẫn kết thúc bằng chấm):
```svg
<path class="bp-t" d="M556 174L590 260"/><circle class="bp-ar" cx="590" cy="260" r="4"/>
<circle class="bp-bal" cx="552" cy="152" r="22"/><text class="bp-mono" x="552" y="159" text-anchor="middle">1</text>
```
**Đường kích thước** (hai đường dóng, đường ghi kích thước, hai mũi tên đặc, chữ ký hiệu thay cho số):
```svg
<path class="bp-t" d="M160 452V520M640 282V520M160 506H640"/>
<path class="bp-ar" d="M160 506l22-6v12zM640 506l-22-6v12z"/>
<text class="bp-mono" x="400" y="498" text-anchor="middle">L</text>
```
**Đường tâm** chạy xuyên qua vật: `<path class="bp-cl" d="M330 70V490"/>`.
**Vật đặc có gạch mặt cắt:**
```svg
<defs><pattern id="bpH1" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
  <path d="M0 0V10" stroke="#e7f0f9" stroke-opacity=".55" stroke-width="1.3"/></pattern></defs>
<path class="bp-o" d="..."/><path d="..." fill="url(#bpH1)"/>
```
**Nhãn hình** góc trên trái của hình: `HÌNH n · TÊN` kèm gạch chân nét mảnh. **Bảng kê** (cột SỐ, TÊN, ...) với nét chữ giả là các vạch `stroke-width: 6` khi không cần chữ thật. **Vết cắt A-A** (đường cắt có mũi tên và chữ A ở hai đầu) để nói "tách ra", "nhìn vào bên trong".

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa nằm bên trái (x 120 đến 1040). Hình đặt trong x 1120 đến 1820, y 200 đến 740, căn theo đường tâm của diễn viên `centre` (y 470) và vết nước `water` (tâm 1460, 470); dưới đáy có dải đất gạch chéo (y 760) và đường kích thước (y 796) của style, khung tên ở góc phải dưới.
- Lớp vẽ: nhãn hình, đường tâm, đường di chuyển phantom, đường bao vật (tô giấy), nếp gấp, gạch mặt cắt, nét khuất, kích thước, bóng số.
- Vật là ẩn dụ của chủ đề (deck mẫu: máy bay giấy cho "slide biết bay"). Kích thước ghi bằng chữ (L, B), không ghi số.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 270 đến 990). Chừa dải y 600 đến 660 cho `hl-text` (bản PPTX căn giữa chữ này theo chiều dọc). Nửa trên: các thành phần vẽ như các chi tiết, nối bằng đường phantom có mũi tên, mỗi thành phần một bóng số. Nửa dưới: bảng kê giải thích số.
- Một thành phần = một vật hoặc một tư thế; cùng một vật thì cùng số (đúng tinh thần Morph).

**c. Quy trình hoặc dòng thời gian.** Đặt SVG chồng lên trục y 630 của `timeline`, diễn viên `dim` đã là trục có mũi tên. Mỗi bước một "trạm" (vòng tròn tô giấy có dấu tâm) ở x = 136 + i × 342,4 (5 bước), đường dóng mảnh lên xuống 44px, cung nối giữa hai trạm cao tối đa 30px trên trục (chữ bước lẻ kết thúc ở y 578). Trạm cuối thêm vòng thứ hai. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ của các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Trên slide `stats`, dùng dải đáy y 836 đến 986 dưới mỗi con số: mỗi cột một hình chiếu nhỏ minh họa ý của số (deck mẫu: ba mặt đứng của slide với 3, 5, 7 dòng, nét mảnh dần; vết cắt A-A ở cột "nên tách slide"). Tâm cột: x 384, 960, 1536 (ba số). So sánh hai phương án: hai hình chiếu cạnh nhau cùng tỷ lệ, cùng đường kích thước.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1"` và `style="--d:.3"` (giây trễ), cần `morph-motion.css`. Vẽ theo thứ tự kỹ thuật: đường bao trước, nếp gấp sau, rồi kích thước, bóng số. Không gắn `draw` vào nét đứt (đường tâm, nét khuất, phantom) vì `draw` ghi đè `stroke-dasharray`.
- Kích thước, bóng số, nhãn: bọc `<g class="reveal">` để hiện sau nét.
- Không dùng animation lặp, không đổi màu, không rung lắc. Con dấu đỏ đã có hiệu ứng "đóng dấu" riêng ở slide closing.
- Nhịp gợi ý: đường bao `--d:0`, chi tiết `--d:.45`, mỗi cung của quy trình trễ thêm 0,2 giây; cả hình xong trong khoảng 2 giây để người nói không phải chờ.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề, không lệch khỏi đường tâm và trục của diễn viên.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py` để chắc SVG sang được PowerPoint.
- Rà màu: trong SVG chỉ có `var(--line)`, `var(--line-soft)`, `var(--hair)`, `var(--fill)`, `var(--deep)` hoặc mã trắng xanh tương đương.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành một hình vector, hiện bằng hiệu ứng quét nếu bên trong có `draw`. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.bp-o`), nên đặt tên lớp riêng có tiền tố.
- SVG trên slide `cover`, `section`, `quote`, `closing` chỉ hiện ở bản HTML (script không xuất hình ở các kiểu này). Cần hình bìa trong PPTX thì dựng bìa bằng `data-layout="free"` với `data-stage="cover"`.
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn kỹ thuật ngắn trong SVG, câu chữ cần sửa để ngoài SVG.

## 6. Cấm
- Màu ngoài bảng (kể cả màu đỏ con dấu trong minh họa), gradient màu, bóng đổ màu, render 3D, hiệu ứng glow neon.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề y 90 đến 165.
- Ghi số đo, số liệu bịa trên đường kích thước: dùng chữ ký hiệu (L, B, x) hoặc nhãn "VÍ DỤ".
- Logo phần mềm thật, bằng sáng chế thật, máy của nhà phát minh có thật, chữ ký người thật.
- Câu dài trong SVG; người vẽ thay cho vật được thiết kế.

Phỏng theo lemo-opuscar `styles/blueprint/STYLE.md` (MIT) qua MotionFly.
