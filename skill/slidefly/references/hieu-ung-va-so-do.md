# Hiệu ứng theo động từ và sơ đồ hình học

Mục tiêu: mỗi slide chọn **hình theo ý**, không nhét mọi ý vào "gạch đầu dòng trái + ô nổi bật phải". Mẫu đầy đủ 16 slide: `templates/deck-so-do.html` (style Cobalt Grid, nội dung ví dụ: một workshop nội bộ 90 phút).

## 1. Nạp file

```html
<link rel="stylesheet" href=".../assets/morph-base.css">
<link rel="stylesheet" href=".../assets/morph-layouts.css">
<link rel="stylesheet" href=".../assets/styles/<style>.css">
<link rel="stylesheet" href=".../assets/morph-motion.css">   <!-- hiệu ứng + màu dùng chung -->
<link rel="stylesheet" href=".../assets/morph-viz.css">      <!-- giao diện 8 dạng sơ đồ -->
...
<script src=".../assets/morph-viz-diagrams.js"></script>     <!-- matrix, network, funnel, compare -->
<script src=".../assets/morph-viz.js"></script>              <!-- span, donut, plan, gather + vẽ tất cả -->
<script src=".../assets/morph-engine.js"></script>
<script src=".../assets/morph-nav.js"></script>
<script src=".../assets/morph-audit.js"></script>
<script src=".../assets/morph-steps.js"></script>            <!-- bấm từng bước -->
```

Thứ tự bắt buộc: hai file `morph-viz*` trước engine (engine đo DOM đã vẽ xong); `morph-steps.js` sau engine.

## 2. Chọn hình theo ý

| Nội dung nói về | Dạng | Cách làm |
|---|---|---|
| Thời lượng, ngân sách chia phần | thanh tỷ lệ | `data-viz="span"` |
| Tỷ lệ, cơ cấu điểm | vòng tròn chia phần | `data-viz="donut"` |
| Bản vẽ, kích thước, cộng kiểm | mặt bằng + chuỗi kích thước | `data-viz="plan"` |
| Nhiều việc gộp thành một | các ô dồn về tâm | `data-viz="gather"` + `data-step` |
| Phân loại theo 2 tiêu chí, "ở đâu" | ma trận | `data-viz="matrix"` |
| Một trung tâm, nhiều nhánh | mạng lưới nút | `data-viz="network"` |
| Lọc dần, nhiều lớp kiểm | phễu | `data-viz="funnel"` |
| Trước và sau, sai và đúng | màn quét | `data-viz="compare"` |
| Hai nhóm có phần chung | 2 vòng giao nhau | vẽ tay SVG (xem mẫu slide 4) |
| Thang mức độ, ai làm nhiều hơn | trục + điểm | vẽ tay (mẫu slide 6) |
| Các bước nối nhau, dòng chảy | chuỗi mắt xích + chấm chạy | vẽ tay + `.travel` (mẫu slide 7) |
| Ba yếu tố cùng quyết định | tam giác nút | vẽ tay (mẫu slide 9) |
| Xếp mục vào nhóm | thùng phân loại | `.bin` + `fx-drop` (mẫu slide 10) |
| Dự phòng nhiều tầng | bậc thang + bóng rơi | vẽ tay + `data-at` (mẫu slide 14) |

Không có số thật thì không dùng biểu đồ có số. Hình minh họa không phải số liệu (chấm trong phễu) phải ghi rõ "minh họa".

## 3. Kiểu slide `diagram`

`<section class="slide" data-layout="diagram">`: không style nào định nghĩa tư thế cho kiểu này, nên hình trang trí lui ra cánh gà, sân khấu trống cho sơ đồ. Tiêu đề vẫn ở góc trên như slide nội dung. Muốn giữ vài hình trang trí thì tự viết `data-pose` riêng (cách viết: `co-che-morph.md`; mẫu: khối `<style>` trong `deck-so-do.html`).

Đặt sơ đồ bằng `style="left:..;top:..;width:..;height:.."` (hoặc `right`/`bottom`). Vùng an toàn: x 120..1800, y 270..990.

## 4. Khai báo từng dạng

Mọi biểu đồ có số phải có `data-source="..."` (audit báo `thiếu data-source`). Danh sách cách nhau bằng `|`, số cách nhau bằng `,`.

```html
<!-- span: notes tự xếp trên/dưới, không chồng nhau; data-hot = ô đỏ khi bấm; data-morph-seg + data-morph-id = ô sẽ phóng to sang slide sau -->
<div class="viz" data-viz="span" style="left:120px;right:120px;top:290px;bottom:110px"
  data-values="10,15,20,10,25,10" data-labels="Mở đầu|..." data-sub="00:00 - 00:10|..." data-hot="2"
  data-morph-seg="4" data-morph-id="lab" data-source="Lịch workshop"></div>

<!-- donut: cung vẽ lần lượt, số thứ tự ở giữa mỗi cung -->
<div class="viz" data-viz="donut" style="left:160px;top:290px" data-values="25,25,25,15,10" data-source="..."></div>

<!-- plan: kích thước thật (mm); chuỗi nào cộng không ra đúng cạnh thì tự đỏ + kính lúp ghi số mm thiếu -->
<div class="viz" data-viz="plan" style="left:120px;top:230px;width:740px;height:760px"
  data-w="6000" data-h="8400" data-wall="4000" data-wall-w="100"
  data-top="320,1900,..." data-bottom="..." data-left="..." data-right="..." data-source="..."></div>

<!-- gather: bọc trong khối data-step có class keep; bấm thì các ô bay về tâm -->
<div data-step="1" class="keep"><div class="viz" data-viz="gather" data-n="17" style="left:0;top:0"></div></div>

<!-- matrix: data-cells đọc theo hàng; data-hot = chỉ số ô (đếm từ 0) sáng lên khi bấm. Ký tự < > viết &lt; &gt; -->
<div class="viz" data-viz="matrix" style="left:120px;right:120px;top:290px" data-hot="5"
  data-cols="Có số liệu|Không có số liệu" data-rows="So sánh|Tiến trình|Cấu trúc" data-cells="...|...|...|...|...|..."></div>

<!-- network: data-on = nút (đếm từ 1) sáng khi bấm, data-off = nút nét đứt -->
<div class="viz" data-viz="network" style="left:120px;right:120px;top:240px;bottom:80px"
  data-hub="morph-viz" data-nodes="span|donut|..." data-sub="...|..." data-on="1,2,3" data-off="8"></div>

<!-- funnel: data-dots = mỗi chấm rơi tới đâu: số tầng (đếm từ 0) bị giữ lại, p = lọt xuống đáy -->
<div class="viz" data-viz="funnel" style="left:120px;top:310px;width:900px;height:660px"
  data-stages="Lớp 1|Lớp 2|Được dùng" data-dots="p,0,p,1"></div>

<!-- compare: con thứ nhất = trước, con thứ hai = sau; cần 1 phần tử data-step="1" trên slide để có cú bấm -->
<div class="viz fx fx-up" data-viz="compare" style="left:120px;right:120px;top:290px;height:660px">
  <div class="cmp-panel">...</div><div class="cmp-panel solid">...</div>
</div>
```

## 5. Hiệu ứng theo động từ (`morph-motion.css`)

Mỗi hiệu ứng tự chạy khi slide hiện ra; `--d` là độ trễ thêm (giây).

| Động từ của câu | Class |
|---|---|
| xuất hiện, đi lên | `fx fx-up` / `fx-left` / `fx-right` / `fx-blur` |
| bật ra, nhấn | `fx fx-pop` |
| rơi vào chỗ | `fx fx-drop` |
| bay từ chỗ khác tới (xếp loại) | `fx fx-from` + `--from:translate(..)` |
| kéo dài, mọc lên | `fx fx-growx` / `fx fx-growy` |
| gõ chữ | `fx fx-type` |
| vẽ nét | `draw` trên `path/circle/rect` có `pathLength="1"` |
| đếm, cộng | `count` + `--to:6000` (chữ số do CSS sinh) |
| đóng dấu, chốt | `slam` (+ `--rot`) |
| cảnh báo, lệch | `shake` |
| gạch bỏ | `strike` |
| gọi chú ý | `ping` |
| dòng chảy | `travel` + `offset-path:path('M..')` + `--dur` |
| gộp lại | `gather` + `--to` (bộ `gather` tự tính) |

Màu dùng chung: `--viz-ink`, `--viz-paper` (theo `--fg`/`--bg` của style), `--viz-hot` (đỏ, chỉ cho sai/thiếu/sắp hỏng), `--viz-fill`, `--viz-faint`, `--viz-mono`. Style muốn đổi thì khai báo lại trên `.deck-stage`.

## 6. Bấm từng bước (`morph-steps.js`)

- `data-step="n"`: phần tử chờ lần bấm thứ n trên slide đó. Bấm hết bước mới sang slide sau. Lùi về slide cũ thì slide hiện đầy đủ.
- Slide có `data-at="<số bước đã hiện>"`, dùng để đổi trạng thái: `.slide[data-at="1"] .node.weak { ... }`. Matrix, network, compare đổi trạng thái từ cú bấm đầu tiên (`data-at` khác 0) và giữ nguyên ở các bước sau.
- Nút lùi luôn về slide trước (không lùi từng bước).
- Khối chứa có `data-step` mà không có class `.fx` sẽ ẩn tới lượt; thêm class `keep` nếu muốn nó vẫn hiện (ví dụ các ô `gather` hiện sẵn, bấm mới dồn).
- Trình duyệt tự động (`check-deck.py`) luôn thấy mọi bước đã mở.

## 7. Lỗi hay gặp

| Hiện tượng | Nguyên nhân | Cách sửa |
|---|---|---|
| Bấm rồi mà hơn 1 giây sau mới đổi màu | quy tắc `data-at` bị dính độ trễ xuất hiện của `.fx` | thêm `transition-delay: 0s !important` vào quy tắc `data-at`, hoặc đặt trạng thái lên một khối bọc không có `.fx` |
| Phần tử biến mất dù đã hiện | `.fx` gắn lên khối cao 0px (chỉ chứa phần tử absolute): vùng cắt của hiệu ứng che mất con | cho khối đó `position:absolute` kèm `width/height` thật |
| Chữ `<tên>` biến mất trong sơ đồ tự viết | chèn chữ vào `innerHTML` mà không thoát ký tự | bộ vẽ có sẵn đã tự thoát: viết `<` hay `&lt;` trong data-* đều được; code tự viết thì thoát `< > & "` trước khi chèn |
| Audit báo `tràn khung` với SVG phủ cả sân khấu | SVG 1920x1080 bị tính là mực | cắt `viewBox` đúng vùng có nét, đặt SVG tại đó |
| Audit báo `nhàm: giống hệt 2 slide trước` | 3 slide liền cùng kiểu slide, cùng tư thế, cùng dạng sơ đồ, cùng bộ hiệu ứng | đổi dạng hình cho 1 slide theo bảng mục 2 |
