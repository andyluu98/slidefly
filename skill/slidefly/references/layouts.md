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
| Sơ đồ, biểu đồ chiếm cả vùng thân | `diagram` (hình trang trí dạt ra viền; xem `hieu-ung-va-so-do.md`) |

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

## 12 bố cục mới (morph-layouts-plus.css)

Nạp thêm `<link rel="stylesheet" href=".../assets/morph-layouts-plus.css">` ngay sau `morph-layouts.css`. Deck mẫu đủ 12 kiểu: `templates/deck-bo-cuc.html`.

Mỗi bố cục mới là **biến thể của một kiểu cũ**: engine giữ tên mới ở `data-kind`, đặt kiểu cũ vào `data-layout`. Nhờ vậy style nào cũng tự đặt hình trang trí và tô màu, không phải sửa style. Kiểu nhiều nội dung dùng nội dung của `diagram`, hình trang trí mượn tư thế slide mục lục (dạt ra viền). `data-stage="clear"` cho sân khấu trống hẳn.

| Nội dung | Kiểu mới | Mượn dáng của |
|---|---|---|
| Một con số là cả câu chuyện (bắt buộc ghi nguồn) | `big-number` | hình dạt ra viền |
| Nhiều ý không ngang nhau, một ý nổi bật | `bento` | hình dạt ra viền |
| Ảnh một nửa, chữ một nửa (thêm class `flip` để đổi bên) | `split-photo` | hình dạt ra viền |
| Câu hỏi gợi mở, lời đáp ở cú bấm sau | `qa` | quote |
| Hai trạng thái trước và sau | `before-after` | hình dạt ra viền |
| Quy trình 3-5 bước nối nhau | `process` | hình dạt ra viền |
| So sánh nhiều tiêu chí, một lựa chọn được khuyên | `compare-table` | hình dạt ra viền |
| Trích lời một người cụ thể | `portrait-quote` | quote |
| Mở chương, số chương khổng lồ phía sau | `chapter` | section |
| Xếp hạng, quan trọng nhất ở cuối | `countdown` | hình dạt ra viền |
| Một câu tuyên bố, một cụm được tô | `statement` | quote |
| Kết bài kèm việc cần làm tiếp | `cta` | cover |

Quy tắc chọn: ý nào có dáng riêng thì dùng dáng đó, đừng nhét mọi thứ vào `content`. Không để 3 slide liền nhau cùng một kiểu (audit báo "nhàm").

```html
<!-- big-number -->
<section class="slide" data-layout="big-number">
  <h2 class="title reveal">Tiêu đề ngắn</h2>
  <div class="bignum">
    <p class="fig reveal-scale"><span class="count" style="--to:302"></span></p>   <!-- hoặc chữ: 302<small>mẫu</small> -->
    <div class="say"><p class="lead reveal">Câu giải thích con số</p><p class="src reveal">Nguồn: file, trang, bảng</p></div>
  </div>
</section>

<!-- bento: 4 cột x 2 hàng; wide = 2 cột, tall = 2 hàng, hot = ô màu nhấn; tổng ô phải lấp đủ lưới -->
<div class="bento">
  <div class="cell hot wide tall reveal"><i class="ico" data-icon="..."></i><h3>Ý chính</h3><p>Một dòng</p></div>
  <div class="cell reveal"><p class="big">2</p><p>chú thích</p></div>
  <div class="cell reveal"><h3>Ý phụ</h3><p>...</p></div>
  <div class="cell wide reveal"><h3>Ý dài</h3><p>...</p></div>
</div>

<!-- split-photo: ảnh có nguồn (audit bắt buộc .photo-credit) -->
<section class="slide" data-layout="split-photo">   <!-- class="slide flip" để ảnh sang phải -->
  <img class="split-img" src="img/anh.jpg" alt="" style="--focus: 40% 50%">
  <div class="split-text"><p class="kicker reveal">Nhãn</p><h2 class="title reveal">Tiêu đề</h2><ul class="bullets"><li class="reveal">...</li></ul></div>
  <p class="photo-credit">Ảnh: tác giả, nguồn, giấy phép</p>
</section>

<!-- qa -->
<p class="qa-label reveal">Câu hỏi</p>
<h2 class="qa-q reveal">Câu hỏi?</h2>
<p class="qa-a fx fx-up" data-step="1">Lời đáp.</p>

<!-- before-after: bên "sau" chờ cú bấm -->
<div class="ba">
  <div class="ba-side before reveal-left"><span class="ba-tag">Trước</span><h3>...</h3><ul><li>...</li></ul></div>
  <div class="ba-arrow reveal">&rarr;</div>
  <div class="ba-side after fx fx-right" data-step="1"><span class="ba-tag">Sau</span><h3>...</h3><ul><li>...</li></ul></div>
</div>

<!-- process: 3-5 bước -->
<ol class="process"><li class="reveal"><span class="n">1</span><h3>Bước</h3><p>Mô tả ngắn</p></li></ol>

<!-- compare-table: cột được chọn có class pick; ô đạt dùng span.yes, ô không dùng class no -->
<table class="ctable reveal">
  <thead><tr><th></th><th>Phương án A</th><th class="pick">Phương án B</th></tr></thead>
  <tbody><tr><th>Tiêu chí</th><td>...</td><td class="pick"><span class="yes">...</span></td></tr></tbody>
</table>

<!-- portrait-quote: ảnh chân dung có quyền dùng, hoặc icon -->
<div class="pq">
  <div class="pq-face reveal-scale"><img src="img/nguoi.jpg" alt="Tên"></div>
  <div><p class="quote reveal">"Câu trích."</p><p class="pq-who reveal"><b>Tên người</b>Chức danh, nguồn</p></div>
</div>

<!-- chapter: markup như section, thêm số chương trang trí (aria-hidden để audit bỏ qua) -->
<p class="ch-num reveal-scale" aria-hidden="true">02</p>
<h2 class="title reveal">Tên chương</h2>
<p class="subtitle reveal">Một câu dẫn</p>

<!-- countdown: thứ tự giảm dần, mục cuối là hạng nhất (to nhất) -->
<ol class="countdown"><li class="reveal"><span class="rk">3</span><h3>Tên</h3><p>Giải thích</p></li></ol>

<!-- statement -->
<p class="kicker reveal">Điều cần nhớ</p>
<h2 class="statement reveal">Một câu với <mark>cụm cần nhớ</mark>.</h2>

<!-- cta: dáng slide bìa; câu dẫn ở subtitle, nút ở ô meta -->
<p class="kicker reveal">Bước tiếp theo</p>
<h2 class="title reveal">Lời kêu gọi</h2>
<p class="subtitle reveal">Liên hệ, đường dẫn</p>
<div class="meta cta-actions reveal"><span class="cta-btn primary">Việc chính</span><span class="cta-btn">Việc phụ</span></div>
```

## Ghi chú
- Icon: lấy SVG Lucide (giấy phép ISC) tại `https://unpkg.com/lucide-static@latest/icons/<ten>.svg`, chỉ chép phần bên trong thẻ `<svg>`.
- Không lồng phần tử `data-morph-id` vào trong phần tử `.reveal` khác ở slide đích (nó sẽ bị ẩn theo cha). Đặt `reveal` trực tiếp lên chính phần tử đó.
- Tùy biến nhỏ cho một deck: thêm `<style>` riêng trong file nguồn, không sửa file trong `assets/`.
