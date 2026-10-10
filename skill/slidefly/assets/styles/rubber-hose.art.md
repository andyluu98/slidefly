# Rubber hose 1930: luật vẽ minh họa SVG cho từng slide

Dùng cùng `rubber-hose.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một khung hình của phim hoạt hình đen trắng đầu thời phim có tiếng. Deck mẫu: `gallery/89_demo-rubber-hose.html`.

## 1. Tinh thần
- Cả deck là **một cuộn phim cũ chiếu trong khung phim bo tròn**: giấy ngà, mực gần đen, xước phim dọc, bụi li ti. Mọi thứ trong khung đều "thở" theo nhạc jazz: ngay cả cái cốc, cái bàn.
- **Nhân vật là đồ vật có mặt cười.** Cả vật là thân người: một tấm slide, một cái cốc, một viên đường. Nét đặc trưng: **tay chân ống cao su** (ống đều nét, không khuỷu, không đầu gối), **găng trắng bốn ngón**, **mắt hình bánh** (tròng đen có khoét một góc), **giày đen tròn to**. Cảm xúc nằm ở miệng và một chi tiết phụ (hơi nước, giọt mồ hôi).
- **Chỉ đen, trắng và xám.** Không một sắc màu nào, kể cả ở vết xước phim. Nhân vật giữ hai đầu mút (trắng sáng, đen đậm); nền dùng các bậc xám giữa.
- Không vẽ nhân vật có sẵn của hãng nào, không chép chuột hay mèo nổi tiếng, không đặt đầu cái cốc lên thân người. Khác `silent-film` (phim câm, ảnh thật, khung chữ thoại): ở đây là hoạt hình nét mực và nhạc là động cơ.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Biến CSS | Dùng cho |
|---|---|---|
| Mực | `var(--ink)` #151413 | nét viền, tròng mắt, giày, thẻ tiêu đề |
| Trắng nhân vật | `var(--white)` #FBF9F3 | thân vật, găng, ống tay, lòng ống |
| Giấy ngà | `var(--paper)` #EBE4D1 | nền slide, chữ trên thẻ đen |
| Bóng hình khối | `var(--shade)` #BDB6A6 | một dải xám sáng ở cạnh phải vật |
| Xám nền | `var(--g1)`, `var(--g3)`, `var(--g4)` | tường, sàn, bóng đổ lệch của thẻ |

- **Một dải bóng cứng**, không chuyển sắc, ở phía xa nguồn sáng (nguồn sáng trên trái): vẽ dải `rh-sh` bên trong thân trước, rồi mới vẽ nét viền đè lên.
- Nét viền 6 px cho nhân vật lớn, 4 đến 4,5 px cho vật nhỏ, 3,5 px cho đường chỉ, mũi tên cong đứt `12 9`. `stroke-linecap` và `stroke-linejoin` là `round`.
- **Ống cao su = hai nét chồng nhau:** `rh-tbo` (mực, 17 px) bên dưới và `rh-tbi` (trắng, 8 px) bên trên, cùng một đường dẫn. Chân là một nét mực 10 px (`rh-leg`).
- **Găng trắng:** vẽ mọi bộ phận (lòng bàn tay, ba ngón, ngón cái, cổ tay loe) bằng nét mực dày rồi tô trắng đè lên, để chỉ còn **một đường viền ngoài** (nét trước, tô sau). Thêm ba vạch may ngắn ở mu bàn tay.
- Tô màu bằng **class trong khối `<style>` của deck** (`.rh-k` mực, `.rh-w` trắng, `.rh-sh`, `.rh-g3`), không ghi `fill="var(...)"` trong thuộc tính để bản PPTX đọc được màu. Chữ trên thẻ đen: `rh-lb` (Lobster, trắng) và `rh-bd` (Be Vietnam Pro đậm, trắng).

## 3. Bộ hình mẫu lặp lại
**Mắt hình bánh** (tròng trắng, tròng đen, một nêm trắng khoét ở góc phải trên):
```svg
<ellipse class="rh-eye" cx="112" cy="118" rx="20" ry="26"/>
<ellipse class="rh-k" cx="116" cy="124" rx="12" ry="19"/><path class="rh-w" d="M118 105L131 109L119 120Z"/>
```
**Miệng** có bốn kiểu: cười toác (khối mực kèm lưỡi xám), cười mỉm (một cung), phẳng (một vạch), lo lắng (đường lượn sóng, thêm giọt mồ hôi trắng viền mực). Mỗi vật có một cảm xúc; vật chính cười toác.
**Giày:** elip mực với một chấm sáng nhỏ ở mũi, rộng gấp 2 đến 3 lần bề ngang của chân.
**Thẻ tiêu đề** (khung chữ, danh sách đánh số): nền mực bo 10 px, bên trong một viền trắng mảnh `rh-lw` (`stroke-width: 2.5`) cách mép 6 px, chữ trắng.
**Huy hiệu số:** đĩa trắng viền mực, số bằng `rh-n` (Lobster, mực), nối vật bằng đường mảnh.
**Đồ vật nhân vật:** thân là chính vật (thẻ slide 16:9 bo góc, cốc, viên đường 3 mặt), mặt đặt ngay trên thân, chân dài như ống mì. Cùng một thân đặt hai tư thế (đứng, nhảy) để diễn tả Morph.

## 4. Bốn công thức
**a. Hình chính cho bìa.** Chữ bìa ở trái (x 120 đến 1040). Hình nằm ở nửa phải, **trên tường họa tiết kim cương** (diễn viên `wall`, x 1080 đến 1892, y 28 đến 800) và **sàn bàn cờ** (`floor`, từ y 800). Diễn viên `mug` đứng sẵn ở giữa; SVG vẽ **bạn của nó** ở bên phải (x 1480 đến 1860, y 340 đến 860): chân chạm sàn y 800 đến 830, một tay đập găng với cái cốc, tay kia giơ cờ. Deck mẫu: tấm slide có mặt cười.

**b. Sơ đồ khái niệm (3 đến 5 thành phần).** Hợp nhất trong vùng highlight của `content` (x 1260 đến 1800), SVG ở `left:1260px; top:280px`, rộng 540, cao 700. **Chừa dải y 310 đến 390 (trong SVG) cho `hl-text`**. Nửa trên: một "khung phim" viền mực bo tròn, bên trong tường xám và sàn bàn cờ, cùng một vật ở hai tư thế (đứng và nhảy lên, kèm bóng dưới sàn), cung đứt nối hai tư thế, ba huy hiệu số. Nửa dưới: ba thẻ tiêu đề đen (y 410, 510, 610, mỗi thẻ cao 78) đánh số khớp huy hiệu.

**c. Quy trình hoặc dòng thời gian.** Diễn viên `card` ở slide `timeline` là **dải phim đen có lỗ răng cưa** đúng trục y 630 (dày 48), nên SVG vẽ **các ô** là quả bóng trắng nằm trên dải và **cung đứt** như quả bóng nhảy trong bài hát hát theo. SVG ở `left:120px; top:560px`, cao 140, trục ở y 70. Trạm tại x = 16 + i x 342,4 (5 bước): đĩa mực r 29, bóng trắng r 23, chấm xám lệch. Cung nối cao tối đa 28 px trên đường y 42. **Trạm cuối là sao nổ** ôm quả bóng. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`. Không vẽ nét vào vùng chữ (trên y 26, dưới y 114).

**d. Con số hoặc so sánh.** Slide `stats`: dải đáy y 836 đến 986 nằm trên sàn bàn cờ, dưới ba con số, tâm cột x 384, 960, 1536. Mỗi cột một tấm slide thu nhỏ 192x108 có mặt: càng nhiều ý, thanh chữ càng mảnh (dày 9, 6, 4 px) và vẻ mặt càng căng (cười, bình thường, lo lắng toát mồ hôi); tấm thứ ba bị cắt đôi bằng nét đứt dọc kèm hai mũi tên tách ra. So sánh hai phương án: hai vật đứng cạnh nhau cùng cỡ, một vật cười một vật nhăn.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: đường liền thêm `class="draw" pathLength="1" style="--d:.3"` (cần `morph-motion.css`). Không gắn `draw` vào nét đứt vì `draw` ghi đè `stroke-dasharray`.
- Huy hiệu và trạm hiện kiểu **bật ra** (`fx fx-pop rh-pop`, khai báo `.rh-pop { transform-box: fill-box; transform-origin: center; }`). Nhóm có `transform="translate(...)"` thì bọc thêm một `<g>` ngoài, vì lớp `fx` ghi đè thuộc tính `transform`.
- Nhãn, danh sách, tay và cờ bọc `<g class="reveal">`. Không dùng animation lặp, không rung.
- Nhịp gợi ý: thân và khung `--d:0` đến `.1`, mắt và miệng cùng lúc với thân, huy hiệu `--d:.4 đến .7`, trạm của quy trình cách nhau 0,15 giây; cả hình xong trong khoảng 2 giây để người nói không phải chờ.
- Mỗi hình chỉ cần **một vật chính** và tối đa **một vật phụ**. Hai nhân vật đứng cạnh nhau (đập tay, nhường đường) đã đủ kể một câu chuyện.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"` và thuộc tính `width`, `height` thì xuất thành hình vector. Lớp CSS chỉ được đọc khi selector cuối là tên lớp (`.rh-k`), nên đặt tên lớp có tiền tố. SVG inline xuất sang PPTX trên mọi layout, kể cả `cover`, `section`, `quote`, `closing`.
- `<pattern>` (sàn bàn cờ trong khung phim) phải có `id` duy nhất trong cả deck (`rh4-ck`: số slide đứng trước).
- Chữ trong SVG thành một phần của hình, không sửa được trong PowerPoint: chỉ để nhãn ngắn.

## Kiểm trước khi giao
- Chân nhân vật chạm sàn (y từ 800), hình nằm trong tường hoặc khung phim, không đè chữ, không vào hàng tiêu đề y 90 đến 165.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`.
- Rà màu: trong SVG chỉ có `rh-k`, `rh-w`, `rh-sh`, `rh-g1`, `rh-g3`, `rh-g4`, `rh-pa` và nét mực hoặc trắng. Mắt phải có nêm khoét, găng phải có đúng bốn ngón (ba ngón và ngón cái).
- Khuôn mặt đọc được ở 50 phần trăm phóng: mắt to, miệng đơn giản.

## Mẫu nhanh khi vẽ hình mới
**Tay ống cao su kèm găng** (cùng một đường dẫn cho hai nét; găng đặt ở đầu ống, xoay theo hướng tay):
```svg
<path class="rh-tbo" d="M62 150C30 170 4 150 -20 124"/><path class="rh-tbi" d="M62 150C30 170 4 150 -20 124"/>
```
**Chân dài và giày:** `<path class="rh-leg" d="M118 240C112 300 104 360 98 440"/>` rồi `<ellipse class="rh-k" cx="84" cy="454" rx="40" ry="16"/>` cộng một chấm sáng `rh-w` ở mũi giày.
**Chuyển động cường điệu:** vật nhảy thì kéo giãn thân 10 đến 15 phần trăm theo chiều nhảy, xoay nhẹ 10 đến 15 độ, chân duỗi về phía sau, thêm bóng elip mực mờ dưới sàn (`fill-opacity: .35`) thấp hơn vị trí chân. Vật hạ cánh thì bẹp xuống và rộng ra.
**Nốt nhạc và vạch nhấn mạnh** có sẵn thành diễn viên (`note`, `lines`); đừng vẽ lại trong SVG trừ khi cần đặt đúng chỗ.

## 6. Cấm
- Bất kỳ sắc màu nào (kể cả màu vàng của tem, đỏ của mực), gradient tô vật, bóng mờ, 3D bóng loáng, hiệu ứng làm mịn kiểu hiện đại.
- Vẽ nhân vật có bản quyền hoặc dáng giống một nhân vật nổi tiếng (tai tròn, quần đỏ, mắt nêm đặc trưng một hãng), chép thiết kế, giai điệu hay logo.
- Nhân vật là người cầm cốc hoặc cốc đặt lên đầu người: **cả đồ vật là thân**.
- Đặt hình đè lên chữ của slide, hay cho nét chạy qua hàng tiêu đề.
- Ghi số liệu bịa lên hình: dùng chữ ký hiệu (A, B, 1, 2, 3).
- Câu dài trong SVG; chữ thoại trong bong bóng.

Phỏng theo lemo-opuscar `styles/rubber-hose/STYLE.md` (MIT) qua MotionFly.
