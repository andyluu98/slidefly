# Ukiyo-e: luật vẽ minh họa SVG cho từng slide

Dùng cùng `ukiyoe.css`. Mỗi slide đáng nhớ có một hình SVG inline vẽ riêng theo nội dung, như một "bản in" nhỏ đặt trên cùng tờ giấy washi. Deck mẫu: `gallery/80_demo-ukiyoe.html`.

## 1. Tinh thần
- Cả deck là **một tờ tranh khắc gỗ**: giấy washi, khung viền đôi mực sumi, mảng màu phẳng in từ từng bản khắc riêng, nét khóa (key line) đen đè lên trên. **Giấy là màu trắng**: bọt sóng, chóp tuyết, sương mù là chỗ giấy không in.
- **Phẳng có chủ ý.** Chiều sâu chỉ đến từ các lớp ngang xếp chồng, dải sương, cắt khung táo bạo; không phối cảnh dựng, không đổ bóng, không gradient (trừ bokashi: màu lau mờ dần ở trời và nước).
- Mỗi màu là một bản in nên **lệch khỏi nét khóa 2 đến 3px** (dùng `transform="translate(3 3)"` cho lớp màu, không cho lớp nét).
- Tín hiệu in khắc: dải sóng vảy (seigaiha), sóng cuộn đầu bọt, cây thông tán phẳng, chóp núi hai mảng, mặt trời đỏ, phiến tiêu đề dọc, con dấu đỏ. Người rất nhỏ, dáng phẳng, mặt vài nét.
- Một sắc chủ đạo (chàm Phổ) cho trời, nước; **đỏ son hiếm**: mặt trời, con dấu, một mảnh áo, một thẻ nhớ. Ba bản in cùng bộ khung: ngày (mặc định), đêm (`section`, `quote`), bình minh (`closing`).
- Không chép tranh nổi tiếng nào: không dựng lại bố cục sóng lớn, núi đỏ, cầu mưa.

## 2. Bảng màu, nét, chất liệu
| Vai trò | Giá trị |
|---|---|
| Nét khóa | `var(--sumi)` #211E1B, dày 2,8 (viền), 1,8 (chi tiết), 3 (khung phiến) |
| Giấy, mảnh phiến | #F4EACB (lớp `uk-paper`, `uk-slip`) |
| Chàm Phổ, chàm sẫm, chàm vừa | #1F3F73 (`uk-ind`), #14284F, #2E5088 (`uk-mid`) |
| Xanh nước, xanh nhạt | #4F78A8 (`uk-blue`), #8FB0CB (`uk-pale`), #7FA3C6, #5E86B0 |
| Đỏ son | #C23B2B (`uk-red`), chữ nhấn #9E2A1F |
| Vàng đất, gỗ, thông | #D2A24A, #9A6A3E, #587A4A |

- Lớp CSS dùng tiền tố `uk-` trong `<style>` của deck (xem deck mẫu): `.uk-k .uk-t .uk-g .uk-d .uk-slip .uk-red ...`. Bản PPTX chỉ đọc lớp khi selector cuối là tên lớp.
- **Vảy sóng** (`seigaiha`): các hàng nửa vòng tròn, hàng sau đè hàng trước, mỗi vảy có 3 vòng giấy mờ bên trong (`uk-foam`, stroke giấy .7). Hàng trên nhạt, hàng dưới đậm dần.
- **Mảng tối đôi:** vật có hai mặt chia bằng hai màu chàm (sáng, tối), chóp tuyết khoét giấy. Nét khóa chạy theo đường bao, thêm vài nét ngắn ở chỗ chuyển mặt.
- Chữ trong hình: `var(--font-display)` (Noto Serif 700) cho nhãn, số trong ô vuông đỏ (`uk-num`, chữ giấy trên đỏ); chỉ nhãn rất ngắn (IN HOA tiếng Việt, 22 đến 34px).

## 3. Hình mẫu lặp lại
**Dải sóng vảy** (hàng vảy bán kính 40 đến 50, vòng bọt bên trong):
```svg
<path class="uk-row1" d="M-40 506a40 40 0 1 0 80 0a40 40 0 1 0 -80 0z"/>
<path class="uk-foam" d="M-30 506a30 30 0 0 1 60 0M-20 506a20 20 0 0 1 40 0"/>
```
**Ô vuông đỏ có số** (như con dấu in): `<rect class="uk-red" width="34" height="34"/><text class="uk-num" ...>1</text>`, hoặc ô đỏ khoét giấy bằng `fill-rule="evenodd"` cho con dấu trên trục thời gian.
**Phiến giấy có khung đôi** (`uk-slip` + khung mảnh bên trong cách 8px), thêm một "thẻ" màu ở cạnh trái: tab xanh chàm, đỏ son, chàm vừa.
**Vết bóng ma**: vật ở tư thế cũ vẽ bằng nét đứt `uk-g`, đường đi bằng chấm `uk-d` có mũi tên đặc `uk-ar`. **Vệt gió**: ba nét cong mảnh `uk-t` phía sau vật chuyển động.
**Thuyền, người:** thân gỗ #9A6A3E, dải đỏ ở mạn; người là một hình phẳng chàm sẫm với nón vàng, hai nét mặt. **Sóng cuộn** đã có trong diễn viên `curl`, hình không vẽ lại.
**Con dấu vuông** (mỗi trạm một họa tiết giấy khác nhau, khoét bằng `fill-rule="evenodd"`):
```svg
<rect class="uk-red" x="-22" y="-22" width="44" height="44" transform="translate(3 3)"/>
<rect class="uk-k" x="-22" y="-22" width="44" height="44" style="stroke-width:3"/>
<path d="M-12 -16H12V-8H-12ZM-12 0H12V8H-12Z" fill="#F4EACB" fill-rule="evenodd"/>
```
**Phiến giấy nhỏ:** hình chữ nhật `uk-slip`, khung mảnh trong cách 8px, thẻ màu 20px ở trái, vạch cọ `stroke-linecap: round`.

## Diễn viên của style và vai của chúng quanh minh họa
| Diễn viên | Vai | Gợi ý khi vẽ hình |
|---|---|---|
| `night` | khối màu cho bản in đêm hoặc bình minh | hình không tô lại nền; chữ trong hình dùng màu giấy khi `data-layout` là `section`, `quote` |
| `sky` | trời bokashi ban ngày | hình đặt lên, không vẽ trời thứ hai |
| `sun` | mặt trời đỏ, thành trăng giấy ở bản đêm | một điểm đỏ lớn mỗi slide là đủ |
| `mount`, `kumo` | núi hai mảng, dải sương hoặc dải trục vàng đất | đáy vật trong hình ngang mép sương |
| `wave`, `curl` | vảy sóng, sóng cuộn đầu bọt | vật nổi đặt đáy ngang hàng vảy đầu tiên |
| `pine`, `cartouche`, `seal` | cành thông hắt góc, phiến tiêu đề dọc, con dấu | chừa đúng chỗ, không vẽ lại |

## 4. Bốn công thức (khung 1920x1080)
**a. Bìa:** chữ bìa nằm trái (x 120 đến 1000). Cảnh nền do diễn viên dựng (trời bokashi, núi, sương, vảy sóng, sóng cuộn, thông, mặt trời). Hình nằm ở x 1100 đến 1600, y 378 đến 940: một **vật là ẩn dụ của chủ đề đặt trên mặt nước**, đáy vật ngang mép trên hàng vảy (y 856); deck mẫu: thuyền buồm có cánh buồm là một slide 16:9 bên trong là bản in nhỏ, bóng ma của buồm cũ nét đứt, ba vệt gió. Nhãn "HÌNH 1 · ..." ở trên cùng. Chừa phiến tiêu đề dọc (x 1070 đến 1130, y 120 đến 375).

**b. Sơ đồ khái niệm (3 đến 5 thành phần):** hợp nhất ở vùng highlight của `content` (x 1260 đến 1800, y 280 đến 980). **Chừa dải y 590 đến 670** cho `hl-text`. Nửa trên: một khung tranh đôi có trời bokashi, dải sóng đáy, một vật (mặt trời) hai tư thế, đường chấm, ba ô số đỏ. Nửa dưới: bảng ghi chú, mỗi dòng một ô số đỏ, nhãn ngắn, ký hiệu bên phải, gạch chân đôi (mảnh và đậm).

**c. Quy trình hoặc dòng thời gian:** diễn viên `kumo` (dải vàng đất) là trục ở y 630; đặt SVG chồng lên (left 120, top 560, cao 140). Trạm ở x = 136 + i x 342,4 (5 bước): mỗi trạm một **con dấu vuông đỏ** (44px) khoét họa tiết giấy riêng, đường dóng ngắn lên xuống; cung nối mực giữa hai trạm cao tối đa 30px, mũi tên đặc; trạm cuối thêm khung vuông thứ hai. Ẩn chấm mặc định: `.s-tl .step::before { display: none; }`.
- Không vẽ nét vào vùng chữ các bước (trên y 586, dưới y 674).

**d. Con số hoặc so sánh:** trên `stats`, dải đáy y 840 đến 970. Mỗi cột một **phiến giấy** (210x104) khung đôi, thẻ màu ở cạnh trái cùng màu với số (chàm, đỏ son, chàm vừa), bên trong 3, 5, 7 vạch cọ sumi mảnh dần; cột cuối thêm vết cắt đứt và hai mũi tên tách ra. Tâm cột: x 384, 960, 1536.

## 5. Chuyển động và xuất PPTX
- Nét vẽ dần: nét liền thêm `class="draw" pathLength="1"` và `style="--d:.3"`, cần `morph-motion.css`. Thứ tự đúng với in khắc: **nét khóa trước**, rồi mảng màu hiện bằng `<g class="reveal">`, rồi chữ. Không gắn `draw` vào nét đứt (`uk-g`, `uk-d`).
- Cả hình xong trong khoảng 2 giây. Không animation lặp, không rung, không đổi màu.
- **PPTX:** `<svg>` là con trực tiếp của slide, có `style="left:..px; top:..px"`, `width`, `height` thì xuất thành hình vector. Diễn viên (mặt nạ, vảy sóng) được xuất riêng, tên `!!` để Morph. Chữ trong SVG không sửa được trong PowerPoint: chỉ để nhãn ngắn.
- `<linearGradient>` trong hình dùng id riêng (`ukA2g`); mọi SVG chung một tài liệu nên id không được trùng.

## Kiểm trước khi giao
- Mở deck, đi qua từng slide có hình: nét không chạm chữ, không vào hàng tiêu đề y 90 đến 165, không đè dải `hl-text`.
- `deck.audit()` không báo lỗi; xuất thử `export-pptx.py`; chữ sáng trên nền đêm đạt tương phản 4,5:1.

## 6. Cấm
- Màu ngoài bảng; đỏ son nhiều hơn một điểm nhấn mỗi hình; gradient trơn (trừ bokashi); bóng đổ, ánh sáng trên vật, render 3D, glow.
- Phối cảnh hội tụ (cánh đồng, đường): chỉ lớp ngang song song, nghiêng.
- Hình đè lên chữ, nét chạy qua hàng tiêu đề, câu dài trong SVG.
- Chữ Hán, Nhật thật hoặc giả dạng chữ thật trong phiến tiêu đề: dùng nét cọ trừu tượng.
- Tranh, bố cục, con dấu của nghệ nhân có thật; logo thật; số đo bịa.
- Phần chỉ dành cho video (camera cuộn tranh, âm thanh, nhịp 8 khung mỗi giây, chuyển động liên tục) không áp dụng cho slide.

Phỏng theo lemo-opuscar `styles/ukiyoe/STYLE.md` (MIT) qua MotionFly.
