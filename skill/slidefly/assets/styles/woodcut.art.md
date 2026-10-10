# Tranh khắc gỗ: luật vẽ minh họa SVG cho từng slide

Dùng cùng `woodcut.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một nhát in từ khối gỗ. Deck mẫu: `gallery/71_demo-woodcut.html`.

## 1. Tinh thần
- **Đen là gỗ còn nguyên, trắng là chỗ lưỡi dao đã lấy đi.** Ánh sáng được khắc ra: chỗ sáng là nhiều nhát rộng gần chạm nhau, chỗ tối để nguyên mặt gỗ.
- **Hình hiện ra bằng cách khắc**, không mờ dần: nhát thô (U) trước, nhát mảnh (V) sau, chấm đục cuối cùng.
- **Mảng lớn, nét thô.** Không chi tiết nhỏ li ti, không gradient. Hình chủ thể là bóng đen có viền dao trắng, hoặc mảng trắng khắc nét đen.
- **Một màu nhấn duy nhất** (cam đồng cháy) và chỉ in **trong vùng đã khắc trắng**, như ánh nắng hay ô cửa sáng đèn; không rải làm trang trí.
- Khác `dong-ho` (tranh Đông Hồ: mảng màu phẳng, viền đỏ) và `paper-ink` (mực trên giấy, nét mảnh): ở đây gần như chỉ đen và giấy kem, nét đục dày và có hướng.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Mực, mặt gỗ chưa khắc | `var(--ink)` (#14110d) |
| Giấy, nhát đã khắc | `var(--paper)` (#efe5d0) |
| Tấm màu duy nhất | `var(--orange)` (#e0612b); chữ cam trên nền đen dùng `var(--orange-text)` |
| Chữ cam trên giấy | `var(--accent)` của style (gạch nung, đủ tương phản) |

- Bốn loại dao, độ rộng trên khung 1920x1080: **dao nhọn** 1,5 đến 2,5px (viền, đường gấp); **đục V** 3 đến 8px (gạch bóng, tóc, nếp); **đục U** 10 đến 20px (tia nắng, quét trời, nhát phá thô); **chấm đục** bán kính 2 đến 5px (tuyết, tia lửa, sao).
- Mỗi nhát là một **hình lá**: gốc to, ngọn nhọn, ngắn 30 đến 160px, không bao giờ là đường dài đều. Tô `var(--paper)` bằng `<path class="wc-p">`, gom cả loạt nhát vào một `d`.
- **Gạch bóng theo hình:** nét chạy theo mặt (sườn núi thì song song mép sườn, mặt cầu thì theo cung). **Độ rộng theo độ sáng:** sáng thì nhát rộng, tối thì không khắc. Chỉ khắc 3 đến 6 nhát sát mép hướng sáng; khắc kín mặt sẽ thành lông hay mưa.
- **Viền dao trắng** quanh vật đen đặt trên nền đen: vẽ `.wc-halo` (tô giấy, viền giấy 15px) rồi vẽ lại bóng đen `.wc-i` đè lên, để chỉ còn viền trắng ngoài.
- Vân gỗ, sợi mực lệch, vệt giấy đã có ở diễn viên `slab`; minh họa không vẽ lại.
- Khai báo lớp trong `<style>` của deck (`.wc-i .wc-p .wc-pk .wc-halo .wc-pbk .wc-pr .wc-orange .wc-ring .wc-tab .wc-lb .wc-it`, xem deck mẫu) để bản PPTX đọc được màu và nét.

## 3. Bộ hình mẫu lặp lại
**Một nhát đục** (gốc rộng, ngọn nhọn; lấy 6 điểm mỗi bên, độ rộng nửa nhát = w x (1 - 0,5 u) x sin(pi u)^0,55):
```svg
<path class="wc-p" d="M40 80L66 74L92 72L118 75L140 80L118 83L92 86L66 86Z"/>
```
**Tia nắng khắc:** các nhát U tỏa từ tâm, dài ngắn xen kẽ (nhát dài 17px, nhát ngắn 9px), đĩa màu cam ở lõi viền một vòng giấy.
**Dải chấm đục:** những hình thoi nhỏ (4 điểm) rải thưa dần theo hướng bay, thu nhỏ từ 5,5 xuống 1,7px.
**Quét trời:** hai đến ba nhát U rất dài (200 đến 350px, rộng 8 đến 13px) lệch nhau, gợi tốc độ.
**Mặt cắt trắng, nét đen:** hình chữ nhật `.wc-pbk` (giấy) rồi các nhát đen `.wc-i` đè lên: dùng làm thẻ, khung, nhãn trên nền đen.
**Ô cửa sáng đèn:** nhà đen có viền giấy 2px, một ô cửa nhỏ tô `.wc-orange`; là chỗ duy nhất có màu trong cảnh.
**Nhãn hình:** `HÌNH n · TÊN` chữ `var(--font-display)` (Anton) tô giấy, gạch chân bằng một nét dao `.wc-pk`.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở bên trái (x 120 đến 1040).
- Hình nằm trên khối đen của diễn viên `slab` (x 1080 đến 1860, y 70 đến 1010) và đĩa mặt trời `sun` (tâm 1470, 420, bán kính 260). SVG đặt left 1100, top 90, rộng 760, cao 940.
- Lớp vẽ: quét trời, dải chấm đục đường bay, vật chính (bóng đen, quầng trắng, vài nhát gạch ở mép sáng), nếp gấp bằng nét dao. Dãy núi `hills` ở đáy đã có sẵn.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Trên slide `content`, đặt trong tấm đen `slab` (x 1230 đến 1840, y 250 đến 1010), tức vùng điểm nhấn x 1260 đến 1800.
- Chừa dải y 560 đến 680 cho `hl-text` chữ giấy.
- Nửa trên: tư thế cũ chỉ là nét dao đứt, tư thế mới là mảng trắng khắc nét đen, mũi tên cong màu cam (vật đang chuyển).
- Nửa dưới: bảng kê khung giấy, mỗi hàng một số trong vòng, tên chữ nghiêng, một dấu hiệu.

**c. Quy trình hoặc dòng thời gian.** Diễn viên `bar` (y 612 đến 648) là trục: dải mực rách.
- SVG left 120, top 560, cao 140, trạm ở x = 136 + i x 342,4.
- Trạm là đĩa mực viền giấy, **mỗi trạm khắc thêm nhát hơn trạm trước** (trơn, 5, 9, 14 nhát, cuối cùng tô cam với 18 nhát đen): đúng ý "khắc là thời gian".
- Cung nối bằng mũi tên đen phình thon cao tối đa 30px trên trục. Ẩn chấm mặc định bằng `.step::before { display: none; }` (đã có trong style).

**d. Con số hoặc so sánh.** Trên slide `stats`, dải đen `slab` (y 824 đến 1044) mang ba tờ giấy 220x112 tâm tại x 384, 960, 1536.
- Mỗi tờ có các nhát đen thay dòng chữ: 3 nhát dày, 5 nhát vừa, 7 nhát mảnh.
- Dưới mỗi tờ là một chú thích chữ nghiêng 22px. Đặt SVG tại left 120, top 836.

## 5. Chuyển động và xuất PPTX
- Hình hiện bằng `<g class="reveal">`; nét có `stroke` vẽ dần bằng `class="draw" pathLength="1"` và `style="--d:.3"` (cần `morph-motion.css`). Các nhát khắc là hình tô nên không vẽ dần.
- Nhịp gợi ý: vật chính trước, gạch bóng và viền, rồi nhãn; cả hình xong trong khoảng 2 giây.
- Không đặt thuộc tính `transform` trực tiếp lên phần tử có lớp `reveal` (CSS của lớp này ghi đè và mất vị trí): bọc thêm một `<g transform>` bên trong.
- Không animation lặp, không rung. Khi đổi slide, mặt trời và núi đã tự trượt bằng diễn viên.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` cùng `width`, `height`, `viewBox` thì thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.wc-p`). Dùng `<g transform>` được; không dùng filter.
- SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- Chữ trong SVG thành một phần của hình, không sửa được: chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165.
- Chữ giấy trên nền đen và chữ mực trên giấy đều đọc rõ; chữ cam chỉ ở nền đen hoặc dạng `--accent` gạch nung trên giấy.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`.
- Rà màu trong SVG: chỉ `var(--ink)`, `var(--paper)`, `var(--orange)`.

## 6. Cấm
- Gradient, bóng đổ mờ, xám trung gian, màu thứ hai ngoài cam, nhiều hơn một tấm màu.
- Màu cam in lên vùng đen chưa khắc, hay dùng cam làm nền trang trí.
- Nét dài đều như vẽ máy, khắc kín mọi mặt, khuôn mặt đen có nét trắng khó đọc (da khắc trắng, nét mặt để đen).
- Ảnh chụp rồi lọc ngưỡng đen trắng, chữ tiếng Việt vẽ ngược trừ khi cố ý làm khối in.
- Hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề.
- Chép lại bản khắc của Masereel, Ward, Kollwitz hay Doré: chỉ mượn cách làm.

Phỏng theo lemo-opuscar `styles/woodcut/STYLE.md` (MIT) qua MotionFly.
