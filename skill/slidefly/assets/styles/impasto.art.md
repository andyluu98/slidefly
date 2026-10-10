# Sơn dầu impasto: luật vẽ minh họa SVG cho từng slide

Dùng cùng `impasto.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một mảng sơn dầu dày vừa được gạt bằng dao pha màu lên cùng bức tranh của deck. Deck mẫu: `gallery/77_demo-impasto.html`.

## 1. Tinh thần
- Cả deck là **một bức tranh sơn dầu dày** trên vải bố sẫm, đóng khung vàng. Mọi hình đều là **mảng phẳng lớn, mép cắt xiên sắc** do lưỡi dao gạt ra; không có nét viền, không có đường bao mảnh.
- **Bố cục giá trị trước, chất liệu sau.** Hình phải đọc được ở cỡ thumbnail (3 mức sáng tối trở lên); vân sơn chỉ thêm ở khoảng cách gần.
- **Ánh sáng ấm đối với bóng lạnh.** Nền xanh lạnh đậm, đèn và cửa sổ vàng cam ấm; độ bão hòa cao nhất dành cho chủ thể (ô, vật chính của hình), không dành cho nền.
- **Sơn đứng yên, chỉ vật trong câu chuyện mới chuyển động.** Nét xuất hiện từng mảng một, như người vẽ gạt từng nhát.
- Không phải bộ lọc "xoáy kiểu Van Gogh", không phải tranh màu nước (sơn đặc, không trong), không phải vector phẳng có kết cấu phủ lên.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Vải bố, bóng đổ | `#211914`, tối nhất `#1A100B` |
| Chữ, sống sơn sáng | kem `#F3E7D0`, trắng ấm `#FFF2D2` |
| Vàng đèn, khung | `#EDB94E`, `#F6C45C`, `#E9B44C` |
| Cam, nâu đỏ (phản chiếu) | `#E8963C`, `#E8832A`, `#B65A28` |
| Cobalt (trời, nước) | `#1D347A`, `#2A4C9A`, `#3E6BC0`, sáng `#7F9FD8` |
| Đào, hồng nhạt (chân trời) | `#E9B09C`, `#F4C48C` |
| Chủ thể bão hòa | đỏ `#C8301F`, xanh `#2F5FB5`, vàng `#F2B632`, lục `#2F9A6E`, tím hồng `#B03A80` |

- **Nhát dao** = một hình bình hành có hai đầu cắt xiên (xiên 0,2 đến 0,3 lần bề cao), tô một màu có sai lệch sáng tối khoảng 10 phần trăm; đôi khi có mảng thứ hai kéo lẫn vào (cùng màu lệch tông, độ đặc 0,55).
- **Sống sơn** (nơi lưỡi dao ép): một nét sáng 3px, độ đặc 0,55, chạy dọc cạnh trên (hoặc trái) của mảng, màu sáng hơn mảng 45 phần trăm. **Mép sơn tối** (nơi dao nhấc lên): nét 4px độ đặc 0,4 ở cạnh dưới (hoặc phải), tối hơn 45 phần trăm. Ánh sáng luôn từ trên trái.
- **Vệt kéo**: 2 đến 4 nét mảnh 1,5 đến 3,5px độ đặc 0,22 theo hướng nhát dao. **Sơn cạn** ở cuối nhát: 3 đến 4 sợi mảnh nối đuôi, ngắn dần.
- Gradient chỉ làm bằng **bậc thang các nhát dao** (cobalt đến đào đến vàng chia 6 đến 7 dải); không dùng `linearGradient` mượt.
- Phản chiếu trên mặt đường ướt là **chồng các nhát ngang ngắn** dưới nguồn sáng, hẹp dần và nhạt dần xuống dưới, không phải một hình chữ nhật.
- Chữ trong SVG: `var(--font-display)` (Fraunces 600), 24 đến 26px, kem hoặc vàng; chỉ nhãn ngắn. Khai báo lớp `.im-lb .im-sm .im-tag` trong `<style>` của deck để PPTX đọc được; màu mảng ghi bằng thuộc tính.

## 3. Bộ hình mẫu lặp lại
**Nhát dao** (đầu xiên, sống sơn, mép tối):
```svg
<path d="M118 40H300L292 92H110Z" fill="#3E6BC0"/>
<path d="M124 43H292" stroke="#7FA3E0" stroke-width="3.2" stroke-opacity=".55" stroke-linecap="round"/>
<path d="M114 90H284" stroke="#1F3B78" stroke-width="4" stroke-opacity=".4" stroke-linecap="round"/>
```
**Ô nhìn từ trên** (chủ thể bão hòa): 8 múi tam giác xen hai màu (đỏ và kem, xanh và kem, vàng và cam), mỗi múi có cạnh sáng hướng về góc trên trái, cạnh tối ở phía kia; trục nhỏ ở giữa; một bóng tối lệch xuống dưới phải độ đặc 0,35.
**Vệt nhát màu** (đuôi bay, đường nối): chuỗi hình bình hành nhỏ xoay theo tiếp tuyến của đường cong, to dần về phía đích, màu xen đỏ, vàng, cobalt, lục, tím hồng, cam.
**Vòng nhát đứt** (bản "mờ" của một vật): 12 đến 14 nhát ngắn xếp quanh một vòng tròn, kem độ đặc 0,6, nhát xoay theo tiếp tuyến.
**Bảng pha màu** (chú thích): bảng gỗ óc chó `#4A3626` hình thận, có lỗ ngón cái, ba nhát sơn màu và nhãn chữ bên phải.
**Máy bay giấy** (vật bay của bìa): ba mảng dao chung một mũi: cánh trên kem `#F3E7D0`, cánh dưới kem tối `#B5A27C`, nếp gấp nâu `#7B6A4E`; sống sơn trắng `#FFFFFF` độ đặc 0,75 dọc mép trên, nét tối `#1E160F` ở nếp gấp.
**Số trong vòng tròn**: nền vải bố `#211914`, viền vàng `#EDB94E` 3px, số `var(--font-display)` đậm; đặt cạnh mỗi tư thế, cùng vật thì cùng số.
**Nhãn tư thế**: cụm 2 đến 3 chữ (ví dụ "Tư thế A"), 24px màu `#C8B79B`, đặt dưới vật, không xuống dòng.
**Hàng ô nhỏ** (số lượng): ô bán kính 15 đến 35, không bóng đổ, xen ba cặp màu theo thứ tự đỏ, xanh, vàng.
**Ngôi nhà ánh đèn** đã có sẵn ở sân khấu (`facade`, `street`, `lamp`): minh họa không vẽ lại, chỉ chừa chỗ.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở bên trái (x 150 đến 1020, trên vải bố trống). Tranh sân khấu chiếm x 1040 đến 1850, y 74 đến 1005 (trời, tòa nhà, đường ướt, đèn, ba cái ô). Hình riêng của slide nằm trong vùng trời: x 1070 đến 1710, y 120 đến 460, trên nền cobalt để nét kem nổi. Deck mẫu: một chiếc máy bay giấy gấp bằng ba mảng dao (kem, kem tối, nâu), kéo theo vệt nhát nhiều màu.
- Lớp vẽ: vệt nhát, cánh dưới và nếp gấp, cánh trên, sống sơn trắng ấm, vệt kéo. Không chạm vào mặt trời và tòa nhà (x từ 1560, y từ 300).

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Vùng highlight của `content`, x 1260 đến 1800, y 280 đến 980; chừa dải y 580 đến 680 cho `hl-text`. Nửa trên: cùng một vật hai tư thế (vòng nhát đứt nhỏ, và chiếc ô đỏ lớn nghiêng) nối bằng vệt nhát vàng cam, số trong vòng tròn nền vải bố viền vàng. Nửa dưới: bảng pha màu với ba nhát sơn, mỗi nhát là một thuộc tính (vị trí, cỡ, màu). Cùng vật thì cùng số.

**c. Quy trình hoặc dòng thời gian.** SVG đặt `left:120px; top:560px`, cao 140, chồng lên trục y 630 (diễn viên `smear` là nhát dao trục). Trạm thứ i trong 5 cột: x = 16 + i x 342,4, y 70: một chiếc ô nhỏ (bán kính 25), xen đỏ, xanh, vàng. Giữa hai trạm là vệt nhát vàng cam vòng lên cao tối đa 30px trên trục (chữ bước lẻ kết thúc y 578); trạm cuối thêm vòng nhát đứt vàng. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét nào vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh.** Slide `stats`, dải đáy y 836 đến 986 dưới mỗi con số: số ô tỷ lệ với ý của số (deck mẫu: 3 ô to, 5 ô vừa, 7 ô nhỏ, màu xoay vòng). Tâm cột: x 384, 960, 1536. Không thêm số mới vào hình.

## 5. Chuyển động và xuất PPTX
- Hình lớn hiện cả cụm: bọc `<g class="reveal">` (cần `morph-motion.css`). Nét đường liền có thể thêm `class="draw" pathLength="1" style="--d:.3"`; không gắn `draw` vào nét đứt. Thứ tự: nền, vệt nhát, chủ thể, nhãn.
- Không animation lặp, không rung, không xoay liên tục, không hiệu ứng "sôi" nét: sơn tĩnh là sơn tĩnh.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height` thì xuất thành hình vector. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`. Chữ trong SVG không sửa được trong PowerPoint: chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không phủ vùng `hl-text`.
- `deck.audit()` báo OK mọi slide; xuất thử `export-pptx.py` không lỗi.
- Rà màu: chỉ dùng màu trong bảng; chủ thể bão hòa không quá 3 màu mỗi hình.
- Rà chất liệu: mọi mảng có đầu xiên và ít nhất một sống sơn sáng; không có mảng nào là hình chữ nhật vuông vức hay hình tròn hoàn hảo.
- Rà nền: hình riêng của slide không nên đặt lên vùng sáng của trời nếu nét của nó cũng sáng (nét kem trên đào sẽ chìm); chọn vùng cobalt đậm.
- Rà kích thước tệp: một SVG của slide dưới 12 KB; nhiều hơn thì giảm số nhát phụ và vệt kéo.
- Rà chữ: nhãn trong SVG cao 24 đến 26px, tương phản với nền từ 4,5:1; cụm dài hơn 4 chữ thì đưa ra ngoài SVG.
- Rà khung: không vẽ gì đè lên viền khung vàng (x dưới 54 hoặc trên 1866, y dưới 54 hoặc trên 1026).

## 6. Cấm
- Nét viền mảnh quanh hình, gradient mượt, bóng mờ (blur), glow neon, hiệu ứng thủy tinh, render 3D, bộ lọc "tranh sơn dầu" lên ảnh.
- Hạt nhiễu phim phủ toàn hình (nhiễu cộng nén sẽ ăn mất mép dao).
- Chữ nhỏ vẽ bằng nhát dao; câu dài trong SVG; hình đè lên chữ của slide.
- Số liệu bịa trong hình: chỉ dùng số ô khớp với số trong slide.
- Sao chép bố cục, hình ảnh hay nhân vật của tranh, phim có thật.

Phỏng theo lemo-opuscar `styles/impasto/STYLE.md` (MIT) qua MotionFly.
