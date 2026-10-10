# SlideFly: slide biết bay

Skill cho [Claude Code](https://claude.com/claude-code) tạo **slide HTML có hiệu ứng chuyển cảnh kiểu PowerPoint Morph**: hình trang trí trượt, phóng to, đổi màu liền mạch giữa các slide. Một file HTML, mở bằng Chrome là trình chiếu được. Có **57 style**, bố cục tự lấp đầy theo lượng chữ và tự đo độ trống của từng slide.

*A Claude Code skill that builds single-file HTML decks with PowerPoint-Morph-like transitions: 85 styles, auto-filling layouts and an automatic fill/overflow audit. Docs are in Vietnamese.*

**Xem trực tuyến:** [Thư viện 85 style](https://andyluu98.github.io/slidefly/gallery/00-gallery.html) · [Deck mẫu 20 slide (Stencil & Tablet)](https://andyluu98.github.io/slidefly/examples/ai-agent-stencil-tablet-20-slide.html) · [Deck mẫu 15 slide (Swiss Modern)](https://andyluu98.github.io/slidefly/examples/ai-agent-swiss-15-slide.html)

![Thư viện style](docs/gallery.jpg)

## Cơ chế trong một câu

Mỗi style có một nhóm hình cố định gọi là **diễn viên**. Mỗi kiểu slide (bìa, mục lục, nội dung, hai cột...) quy định một **tư thế** cho các diễn viên. Khi chuyển slide, trình duyệt cho diễn viên trượt dần sang tư thế mới, đúng tinh thần Morph: cùng tên là cùng một vật.

## Tính năng

- **85 style:** 10 preset và 30 bold template phỏng theo [frontend-slides](https://github.com/zarazhangrui/frontend-slides), 1 style tái tạo mẫu Morph "vòng tròn xanh", và 10 style mới: 3 style bản sắc Việt (sơn mài, tranh Đông Hồ, Hội An), 5 style xu hướng 2026 (aurora, bento, bauhaus, restorative, wabi), 2 style cho dịp đặc biệt (art deco, clay 3D), và 34 **style hai lớp** phỏng theo [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) qua MotionFly (blueprint, thủy mặc, màu nước, cắt giấy đỏ, bảng trắng, kể chuyện số liệu, HUD hologram, tranh khắc gỗ, kính màu, phim câm, sách tranh sáp màu, ukiyo-e, đèn lồng giấy, múa rối bóng, pixel RPG, anime 80s...): ngoài lớp CSS còn có bản luật `.art.md` để Claude vẽ minh họa SVG riêng cho từng slide. Mọi font đều có bộ chữ tiếng Việt.
- **10 kiểu slide:** cover, agenda, section, content, two-col, stats, timeline, quote, closing, và `diagram` (sơ đồ chiếm cả vùng thân, hình trang trí dạt ra viền).
- **8 dạng sơ đồ tự vẽ từ số liệu:** thanh tỷ lệ, vòng tròn chia phần, mặt bằng có chuỗi kích thước, các ô dồn về tâm, ma trận, mạng lưới nút, phễu lọc, màn quét trước và sau. Khai báo bằng vài thuộc tính `data-*`, biểu đồ có số phải ghi nguồn.
- **Hiệu ứng theo động từ:** vẽ nét, đếm số, đóng dấu, rơi vào chỗ, bay vào nhóm, gộp về tâm, rung khi lệch, chấm chạy dọc đường ống.
- **Icon Tabler:** hơn 5.000 icon MIT (có logo công cụ như Python, GitHub) khai báo bằng một dòng; `icons.py suggest` gợi ý icon theo chữ trên slide, kể cả từ tiếng Việt; audit chặn slide quá 6 icon.
- **21 dáng slide:** 9 kiểu gốc và 12 kiểu mới (số lớn, bento, ảnh chia đôi, hỏi đáp, trước và sau, quy trình, bảng so sánh, trích dẫn có chân dung, chương, đếm ngược, tuyên bố, kết có lời kêu gọi). Kiểu mới chạy trên cả 57 style mà không phải sửa style.
- **12 khung bố cục phá lưới:** `data-frame` đổi hẳn cách chia mặt slide: mảng màu một bên (split-left, split-right), tiêu đề khổng lồ (poster), dải ngang (band), cột tiêu đề (rail), tiêu đề cuối slide (bottom), cột hẹp (stack), khối góc (corner), mảng chéo (diagonal), khung viền (frame), thẻ so le (zigzag), số lớn (numbered). Nội dung nào cũng tự chạy vào vùng của khung; đã kiểm trên cả 57 style. Mẫu: `templates/deck-khung.html`.
- **Logo xuyên suốt:** một logo (icon Tabler hoặc file ảnh) to ở bìa, thu về góc ở slide nội dung, ẩn ở slide trích dẫn, và tự bay giữa các vị trí đó.
- **Khung giao diện giả:** cửa sổ chat, terminal, trình duyệt, điện thoại vẽ bằng CSS. Prompt gõ từng chữ, trợ lý "nghĩ" rồi trả lời từng dòng, lệnh cài hiện dần theo cú bấm.
- **Slide ảnh nền và lưới icon:** ảnh tràn màn hình làm điểm nghỉ giữa các phần (lớp phủ giữ chữ dễ đọc, bắt buộc ghi nguồn ảnh); lưới 3 đến 6 icon cùng màu cho các ý ngắn.
- **Không rập khuôn:** `pick-styles.py` gợi ý 3 style (hợp mục đích, khác nền, bất ngờ) và một cách kể chuyện, xáo mỗi lần chạy, nên cả lớp gõ cùng một prompt vẫn ra các bộ slide khác nhau. Deck dài thêm `--parts N`: mỗi phần một nhịp kể riêng, slide chương xen kẽ nền.
- **Bấm từng bước:** `data-step` cho phép giảng tới đâu mở tới đó, phím lùi gỡ đúng một bước; slide có `data-at` để đổi trạng thái theo từng cú bấm.
- **Tự lấp đầy:** engine đếm số ý trên slide rồi chọn cỡ chữ lớn, vừa hoặc nhỏ. Slide nội dung có ô điểm nhấn, slide hai cột có câu kết luận.
- **Không lặp nhàm:** cùng một kiểu slide xuất hiện nhiều lần sẽ đổi dáng (biến thể 1, 2, 3) và đổi hướng chữ vào khung. Slide sơ đồ, bento, bảng so sánh vẫn giữ hình trang trí của style ở viền thay vì để sân khấu trống. Tiêu đề có hai biến thể: đặt giữa (`data-title="center"`) và chạy dọc mép trái (`data-title="side"`); slide nào cũng có thể mượn tư thế của kiểu khác bằng `data-stage`.
- **Slide tự thiết kế:** `data-layout="free"` cho sân khấu trống để AI tự dựng bố cục riêng bằng CSS của deck (chữ khổng lồ cắt mép, lưới bất đối xứng, timeline uốn lượn...). Skill coi đồ nghề có sẵn là gợi ý, không phải khuôn, nên mỗi deck có vài slide mang dáng riêng (`references/tu-thiet-ke.md`).
- **Chữ bay giữa hai slide (FLIP):** ví dụ tiêu đề mục ở trang mục lục bay sang thành tiêu đề phần.
- **Tự kiểm tra ngay trong trang:** mở deck rồi gõ `deck.audit()` trong console (hoặc để Claude gõ qua trình duyệt của app): đo khoảng trống và chữ tràn, độ tương phản của chữ với hình phía sau và với khung chứa nó, slide lặp dáng, biểu đồ thiếu nguồn. Không cần cài gì thêm.
- **Xuất PowerPoint có Morph:** `scripts/export-pptx.py` ghi file .pptx sửa được, hình trang trí cùng tên qua các slide nên PowerPoint Morph cho chúng bay như bản HTML.
- **Không phụ thuộc thư viện:** chỉ HTML, CSS, JavaScript thuần. Có chế độ giảm chuyển động.

## Cài đặt

```bash
git clone https://github.com/andyluu98/slidefly.git
cp -r slidefly/skill/slidefly ~/.claude/skills/
pip install -r slidefly/requirements.txt
```

Python chỉ cần cho các script kiểm tra và đóng gói. Deck tạo ra chạy được trên mọi trình duyệt hiện đại mà không cần Python.

## Cách dùng

Trong Claude Code, gõ `/slidefly` hoặc nói tự nhiên, ví dụ: *"Làm 20 slide giải thích AI Agent, style stencil-tablet"*. Skill sẽ lập dàn ý, chọn kiểu slide, dựng deck, tự kiểm tra rồi đóng gói thành một file HTML.

Dùng thủ công không qua Claude:

1. Chép `skill/slidefly/templates/deck-mau.html`, đổi dòng `<link>` sang style muốn dùng (danh sách ở `assets/styles/index.json`).
2. Thay nội dung các `<section class="slide" data-layout="...">` (markup mẫu ở `references/layouts.md`).
3. Đóng gói: `python scripts/inline-assets.py nguon.html deck.html`
4. Kiểm tra: mở deck trong trình duyệt, gõ `deck.audit()` trong console.

**Trình chiếu:** mũi tên hoặc Space để sang slide, mũi tên trái để lùi, `F` toàn màn hình, `Home`/`End` về đầu/cuối.

## Cấu trúc

```
skill/slidefly/
├── SKILL.md                 quy trình cho Claude
├── assets/
│   ├── morph-engine.js      co giãn khung, diễn viên, biến thể, FLIP
│   ├── morph-nav.js         phím, 2 nút rìa, vuốt (bấm thân slide không chuyển)
│   ├── morph-audit.js       deck.audit(): đo khoảng trống và chữ tràn
│   ├── morph-base.css       khung 1920x1080, chuyển cảnh, hiệu ứng chữ
│   ├── morph-layouts.css    9 kiểu slide tự co giãn
│   ├── morph-layouts-plus.css  12 kiểu slide mới
│   ├── morph-motion.css     hiệu ứng theo động từ + màu dùng chung
│   ├── morph-viz*.js/.css   8 dạng sơ đồ tự vẽ
│   ├── morph-steps.js       bấm từng bước
│   ├── morph-icons.css/.js  icon Tabler (tự tải khi soạn, nhúng khi gộp)
│   ├── morph-brand.css      logo xuyên suốt
│   ├── morph-mock.css/.js   khung chat, terminal, trình duyệt, điện thoại
│   ├── morph-photo.css      slide ảnh nền
│   ├── icons/               danh mục Tabler + từ khóa tiếng Việt
│   └── styles/              85 style (+ .art.md cho style hai lớp) + index.json
├── references/              cơ chế, layout, công thức chuyển cảnh, chọn style, font tiếng Việt
├── scripts/                 inline-assets.py, export-pptx.py, icons.py, pick-styles.py
└── templates/              deck-mau.html (10 slide đủ 9 kiểu), deck-so-do.html (16 slide, mỗi slide một dạng hình), deck-giao-dien.html (10 slide, logo, khung giao diện, ảnh nền, lưới icon), deck-bo-cuc.html (13 slide, 12 bố cục mới)
examples/                    2 deck mẫu về AI Agent
gallery/                     00-gallery.html + 85 deck demo
```

## Ghi nguồn

Các style phỏng theo [frontend-slides](https://github.com/zarazhangrui/frontend-slides) của Zara Zhang (MIT); 6 style hai lớp phỏng theo [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) của LemoLab (MIT), qua [MotionFly](https://github.com/andyluu98/MotionFly). Icon từ [Lucide](https://lucide.dev) (ISC). Font tải từ Google Fonts (SIL Open Font License). Chi tiết ở [THIRD_PARTY.md](THIRD_PARTY.md).

## Giấy phép

[MIT](LICENSE)
