# Lớp minh họa: Infographic isometric (`iso-infographic`)

Luật để vẽ một minh họa SVG inline riêng cho từng slide, cùng chất với sân khấu `iso-infographic.css`. Deck mẫu: `gallery/61_demo-iso-infographic.html` (bìa, sơ đồ khái niệm, quy trình, con số).

## 1. Tinh thần

- **Một sa bàn hệ thống:** mọi thứ đứng trên một tấm nền nổi (board) hoặc một tấm trạm (plate), nhìn từ góc isometric 30 độ cố định. Phép chiếu không bao giờ xoay, nghiêng hay có phối cảnh.
- **Khối phẳng ba tông, không viền:** mỗi khối chỉ có mặt trên sáng, mặt trái vừa, mặt phải tối. Không đổ bóng mềm, không ánh sáng, không gradient trên khối.
- **Đồ nghề infographic là một phần của hình:** đường luồng nét đứt có mũi tên, ghim nhãn (vòng tròn, cần đứng, gạch ngang), vòng theo dõi, đường kích thước, khung trạm nét đứt. Mực chỉ dùng cho những thứ này.
- **Màu mang nghĩa như chú giải bản đồ:** một màu một vai trò, không dùng một màu cho hai nghĩa. Dữ liệu và nước luôn xanh dương; vật đang được kể (chủ thể) luôn san hô.
- **Không có gì di chuyển mà không có đường dẫn trước:** luồng vẽ trước, khối tới sau.

## 2. Bảng màu, nét, chất liệu

| Vai trò | Biến (mặt trên / trái / phải) | Lớp SVG có sẵn |
|---|---|---|
| Dữ liệu, nước, hệ thống | `--blue-t` `--blue-l` `--blue-r` | `.i-bt .i-bl .i-br` |
| Chủ thể (vật đang kể) | `--coral-t` `--coral-l` `--coral-r` | `.i-ct .i-cl .i-cr` |
| Nhóm phụ, bước giữa | `--amber-t` `--amber-l` `--amber-r` | `.i-at .i-al .i-ar` |
| Kết quả, hoàn tất | `--mint-t` `--mint-l` `--mint-r` | `.i-mt .i-ml .i-mr` |
| Trung tính (máy, chữ, giấy) | `--slate-t` `--slate-l` `--slate-r` | `.i-st .i-sl .i-sr` |
| Nền, giấy, mực | `--ground` `--paper` `--ink` | `.i-plate` `.i-ink` `.i-head` `.i-pin` |

- Các lớp `.i-*` nằm sẵn trong `iso-infographic.css`, nên tô màu bằng `class`, không viết `fill="var(--...)"` trong thuộc tính (trình duyệt và bản PPTX đều không đọc).
- Nét: `.i-ink` 3px tròn đầu cho ghim, đường kích thước; `.i-flow` 4px nét đứt 14/10 cho luồng; `.i-ghost` 2,5px nét đứt mờ cho vị trí cũ, lưới ô; `.i-plate` nền giấy viền đứt 10/7.
- Khối đặc không có viền. Không dùng `filter`, `mask`, `marker`, gradient trên khối. Đất ở mép board vẽ bằng 3 đến 4 dải màu nâu phẳng (xem actor `slab`).

## 3. Hình mẫu lặp lại

Phép chiếu: trục u đi xuống phải, trục v đi xuống trái, z đi lên. Với gốc `(ox, oy)` và `k` px mỗi đơn vị:
`x = ox + 0.866·k·(u − v)`, `y = oy + 0.5·k·(u + v) − k·z`. Vẽ theo thứ tự xa trước gần sau (u + v + z nhỏ trước).

**Khối hộp** (ba đa giác, mặt trái, mặt phải rồi mặt trên):
```html
<g><polygon class="i-cl" points="0,30 52,60 52,120 0,90"/>
   <polygon class="i-cr" points="52,60 104,30 104,90 52,120"/>
   <polygon class="i-ct" points="52,0 104,30 52,60 0,30"/></g>
```
**Luồng dữ liệu** (đi dọc trục u hoặc v trên mặt đất, mũi tên là tam giác ép dẹt theo mặt đất, không dùng `marker`):
```html
<path class="i-flow" d="M400 300L560 392"/>
<polygon class="i-head fx fx-pop" style="--d:1" points="583,405 560,392 570,382"/>
```
**Ghim nhãn:** vòng `.i-pin` r 9 ở tâm mặt trên của vật, cần đứng và gạch ngang `.i-ink draw`, nhãn là HTML `.pin-lbl` (thẻ giấy viền mực, bo 8px) đặt ngoài SVG.
```html
<path class="i-ink draw" pathLength="1" d="M1656 537V330H1700"/><circle class="i-pin" cx="1656" cy="537" r="9"/>
```
**Vòng theo dõi:** chỉ nửa trước của elip quanh chân vật (nửa sau bị khối che): `rx = 1.22·R`, `ry = 0.71·R`, `M cx−rx,cy A rx ry 0 0 0 cx+rx,cy`.
**Bóng ma vị trí cũ:** đường viền lục giác `.i-ghost` cùng ba cạnh trong, cho biết vật vừa rời chỗ.
**Gói dữ liệu (Isotype):** khối nhỏ xanh dương cạnh 20 đến 24px đặt giữa luồng; muốn nói số lượng thì lặp đúng số khối, cùng cỡ.
**Đường kích thước:** nét `.i-ink` song song với cạnh vật, cách 30 đến 40px, hai gạch chặn đầu theo trục kia; con số là nhãn HTML.

## 4. Bốn công thức

Khung 1920x1080. Hàng tiêu đề y 90..165 để trống. Lề an toàn 80px hai bên, 60px trên dưới. Đặt `<svg style="position:absolute;left:..px;top:..px" width=".." height=".." viewBox="left top width height">` để vẽ bằng tọa độ slide.

**4.1 Hình chính cho bìa.** Chữ cột trái x 140..960 (style đã đặt `padding` cho bìa). Bên phải là sa bàn của actor (`slab` rộng 820px tại x 1000, y 360, tháp và ba khối đứng trên mặt): minh họa chỉ thêm lớp hệ thống lên đúng tọa độ đó.
- Lớp 1: luồng nối các khối theo hình vuông trên mặt board, cắt đầu cách tâm khối một cạnh khối để không đè lên khối.
- Lớp 2: gói dữ liệu ở giữa mỗi luồng, hiện bằng `fx fx-pop` lệch nhịp.
- Lớp 3: một vòng theo dõi quanh chủ thể, hai ghim nhãn chỉ ra ngoài vùng chữ (lên trên phải, xuống dưới trái).
- Lưu ý: nhãn dùng đúng từ khóa của deck, tối đa hai ghim.

**4.2 Sơ đồ khái niệm (3 đến 5 thành phần).** Mỗi thành phần là một trạm: tấm `.i-plate` hình thoi (cạnh khoảng 170px, dày 14px mặt `.i-sl/.i-sr`) mang một vật tượng trưng. Các trạm xếp zíc zắc dọc trục, tâm cách nhau 485px theo hướng (0.866, ±0.5), nên luồng giữa chúng luôn đi đúng trục.
- Vùng vẽ y 200..800, nhãn HTML `.st-lbl` (tên in hoa, một dòng mô tả) đặt dưới mỗi trạm, rộng 340px.
- Vật tượng trưng gợi ý: chồng tấm mỏng (tệp, cấu hình), cụm khối ba màu (thành phần), lưới 3x3 có bóng ma (vị trí, trạng thái), bóng ma, luồng, khối (thay đổi).

**4.3 Quy trình hoặc dòng thời gian.** Ba đến năm cột khối đứng cùng hàng ngang, đáy y 850, cao dần (100, 200, 300px) để thấy tiến triển; mỗi cột một màu theo vai trò, chủ thể san hô đặt trên mặt cột.
- Luồng nhảy cong từ mặt cột này sang cột sau (`Q` bậc hai, mũi tên theo tiếp tuyến cuối).
- Số bước và nhãn HTML `.pr-num` `.pr-lbl` nằm trên mỗi cột, rộng 400px; luồng phải đi dưới nhãn.
- Dòng thời gian dài: dùng slide `timeline` có sẵn, actor `route` đã thành trục có mũi tên.

**4.4 Con số hoặc so sánh.** Con số lớn là chữ HTML ở cột trái (x 120..860, `.n-big` 116px), câu giải thích và nguồn ngay dưới. Bên phải là vật mang con số trên một tấm trạm: khung màn hình đứng có đường kích thước, hai vật cùng loại khác cỡ, hoặc hàng khối Isotype đếm đúng số.
- So sánh: hai tấm trạm cạnh nhau (trước, sau), cùng góc nhìn, chỉ đổi số khối hoặc chiều cao.
- Không dựng biểu đồ 3D có trục: số luôn đếm được bằng khối hoặc ghi bằng nhãn.

## 5. Chuyển động và xuất PPTX

- Nét ghim, đường kích thước, vòng theo dõi: `class="i-ink draw" pathLength="1" style="--d:.8"` (vẽ dần khi slide active, theo `morph-motion.css`).
- Luồng `.i-flow` tự chạy kiến khi slide active (`.slide.active .i-flow` đổi `stroke-dashoffset`), như dữ liệu đang chảy. Không gắn `draw` cho luồng vì sẽ mất nét đứt.
- Khối, trạm: bọc `<g class="fx fx-up">` hoặc `fx fx-pop` với `--d` lệch nhịp; style đã đặt `transform-box: fill-box` để khối nở từ tâm. Khối đặc tới bằng chuyển động, không mờ dần nửa vời.
- Hệ điều hành bật giảm chuyển động thì luồng đứng yên, nét vẽ nhanh.
- Xuất PPTX: mỗi `<svg>` con trực tiếp của slide có `left/top` trong `style` cùng `width/height` thành một hình vector (PowerPoint 365); màu lấy từ lớp `.i-*`. Chữ trong SVG không sửa được, nên mọi nhãn để ngoài SVG bằng HTML có `left/top/width` trong `style`. Riêng nhãn tự đặt trên slide bìa, mở phần, trích dẫn, kết chưa sang PPTX: muốn giữ thì đưa vào slide `data-layout="free"` (có thể `data-stage="cover"`).

## 6. Cấm

- Màu ngoài bảng trên; một màu cho hai nghĩa; tô san hô cho thứ không phải chủ thể.
- Phối cảnh, xoay hay nghiêng phép chiếu, khối xoay lệch trục, low poly có ánh sáng, bóng đổ mềm, viền quanh khối đặc.
- Chữ, số vẽ trong SVG (`<text>`), chữ đè lên khối; nhãn che chủ thể.
- Biểu đồ 3D có trục, con số không có nguồn, đếm Isotype sai số lượng.
- `marker`, `filter`, `mask`, `mix-blend-mode`, ảnh bitmap trong minh họa.

Phỏng theo lemo-opuscar `styles/iso-infographic/STYLE.md` (MIT) qua MotionFly.
