# 9 kiểu slide: khi nào dùng và markup

Khung 1920x1080. Slide trong (agenda, content, two-col, stats, timeline) có **hàng tiêu đề** y 90..165 và **vùng thân** y 270..990, x 120..1800. Vùng thân luôn được lấp đầy: engine đếm số ý và gắn `data-density`:

| Kiểu | lg (chữ lớn) | md | sm |
|---|---|---|---|
| content, two-col (ý mỗi cột) | 1-3 ý | 4-5 | 6+ |
| agenda, timeline, stats | 1-4 mục | 5-6 | 7+ |

Ghi đè khi cần: `<section ... data-density="lg">`.

## Bảng chọn kiểu slide

| Nội dung | Kiểu |
|---|---|
| Mở đầu, tên bài | `cover` |
| Danh sách phần (2-8 mục) | `agenda` |
| Mở một phần mới | `section` |
| Giải thích 3-6 ý + 1 điểm nhấn | `content` |
| So sánh 2 phía | `two-col` |
| 2-4 con số/khái niệm lớn | `stats` |
| Quy trình, mốc thời gian 3-6 bước | `timeline` |
| Một câu đáng nhớ | `quote` |
| Kết thúc, cảm ơn, tóm tắt 1 dòng | `closing` |

Đổi kiểu liên tục giúp diễn viên chuyển động nhiều hơn. Hai `content` liền nhau vẫn chuyển động nhờ parity chẵn/lẻ.

## Markup

```html
<!-- cover: kicker, title, subtitle, meta (đều tùy chọn trừ title) -->
<section class="slide" data-layout="cover">
  <p class="kicker reveal">Nhãn nhỏ</p>
  <h1 class="title reveal">Tiêu đề bài</h1>
  <p class="subtitle reveal">Một câu mô tả</p>
  <p class="meta reveal">Người trình bày, ngày</p>
</section>

<!-- agenda: title PHẢI là phần tử đầu tiên; li tự chia 2 cột.
     reveal đặt trên từng con, KHÔNG đặt trên li (h3 có data-morph-id không được nằm trong cha bị ẩn) -->
<section class="slide" data-layout="agenda">
  <h2 class="title reveal">Nội dung</h2>
  <ol class="agenda-list">
    <li><span class="num reveal">01</span><div><h3 class="reveal" data-morph-id="s1">Tên phần</h3><p class="reveal">Mô tả ngắn</p></div></li>
  </ol>
</section>

<!-- section: số lớn + tiêu đề; data-morph-id trùng với agenda để chữ bay sang -->
<section class="slide" data-layout="section">
  <p class="num reveal">01</p>
  <h2 class="title reveal" data-morph-id="s1">Tên phần</h2>
  <p class="subtitle reveal">Một câu dẫn</p>
</section>

<!-- content: bullets trái + highlight phải (BẮT BUỘC có highlight) -->
<section class="slide" data-layout="content">
  <h2 class="title reveal">Tiêu đề</h2>
  <ul class="bullets">
    <li class="reveal"><b>Từ khóa</b>: giải thích ngắn.</li>
  </ul>
  <aside class="highlight reveal-scale">
    <div class="hl-icon"><svg viewBox="0 0 24 24">...icon Lucide...</svg></div>
    <!-- hoặc <p class="hl-big">16:9</p> khi có số/chữ ngắn có nguồn -->
    <p class="hl-text">Câu chốt 3-7 từ</p>
  </aside>
</section>

<!-- two-col: 2 thẻ cao hết vùng; takeaway khi mỗi cột <= 3 ý -->
<section class="slide" data-layout="two-col">
  <h2 class="title reveal">Tiêu đề</h2>
  <div class="cols">
    <div class="col reveal-left"><h3>Bên A</h3><ul><li>...</li></ul></div>
    <div class="col reveal-right"><h3>Bên B</h3><ul><li>...</li></ul></div>
  </div>
  <p class="takeaway reveal">Câu kết luận một dòng.</p>
</section>

<!-- stats: 2-4 mục; stat-num là số có nguồn hoặc ký hiệu ngắn (01, 4-5, 6+) -->
<section class="slide" data-layout="stats">
  <h2 class="title reveal">Tiêu đề</h2>
  <div class="stats">
    <div class="stat reveal"><span class="stat-num">01</span><span class="stat-label"><b>Tên</b>: mô tả 1-2 dòng</span></div>
  </div>
</section>

<!-- timeline: 3-6 bước, lẻ ở trên trục, chẵn ở dưới -->
<section class="slide" data-layout="timeline">
  <h2 class="title reveal">Tiêu đề</h2>
  <div class="timeline">
    <div class="step reveal"><div class="when">01</div><h3>Tên bước</h3><p>Mô tả ngắn</p></div>
  </div>
</section>

<!-- quote -->
<section class="slide" data-layout="quote">
  <blockquote class="quote reveal-blur">Câu trích hoặc câu chốt.</blockquote>
  <p class="cite reveal">Nguồn thật, hoặc "Cách nhớ nhanh" nếu là câu tự viết</p>
</section>

<!-- closing -->
<section class="slide" data-layout="closing">
  <p class="kicker reveal">Tóm lại</p>
  <h2 class="title reveal">Cảm ơn</h2>
  <p class="subtitle reveal">Thông điệp cuối một dòng.</p>
</section>
```

## Ghi chú
- Icon: lấy SVG Lucide (giấy phép ISC) tại `https://unpkg.com/lucide-static@latest/icons/<ten>.svg`, chỉ chép phần bên trong thẻ `<svg>`.
- Không lồng phần tử `data-morph-id` vào trong phần tử `.reveal` khác ở slide đích (nó sẽ bị ẩn theo cha). Đặt `reveal` trực tiếp lên chính phần tử đó.
- Tùy biến nhỏ cho một deck: thêm `<style>` riêng trong file nguồn, không sửa file trong `assets/`.
