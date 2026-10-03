# Font Google có bộ chữ tiếng Việt (đã kiểm 03/10/2026)

Cách kiểm: tải `https://fonts.googleapis.com/css2?family=<Ten+Font>` với User-Agent Chrome, có chuỗi `/* vietnamese */` là đạt. Chỉ dùng font trong danh sách này; font khác phải kiểm trước.

| Nhóm | Font đạt |
|---|---|
| Sans hiện đại | Inter, Be Vietnam Pro, Montserrat, Manrope, Plus Jakarta Sans, Work Sans, Space Grotesk, Archivo, Archivo Narrow, Bricolage Grotesque, Hanken Grotesk, Barlow, IBM Plex Sans, Open Sans, Nunito, Mulish, Lexend, Epilogue, Geologica, Raleway, Josefin Sans, Kanit, Prompt, Bai Jamjuree, Darker Grotesque, Quicksand, Comfortaa, Encode Sans Expanded, Exo 2 |
| Hẹp, cao, poster | Oswald, Anton, League Gothic, Fjalla One, Barlow Condensed, Saira Condensed, Roboto Condensed, Big Shoulders Display |
| Đậm, khối, vui | Unbounded, Dela Gothic One, Paytone One, Bungee, Baloo 2, Alfa Slab One |
| Stencil | Big Shoulders Stencil Display, Saira Stencil One |
| Serif | Playfair Display, Playfair Display SC, Fraunces, Lora, Newsreader, Cormorant, Cormorant Garamond, Source Serif 4, Literata, Noto Serif, Alegreya, EB Garamond, Spectral, Merriweather, Libre Bodoni, Roboto Slab |
| Viết tay, script | Patrick Hand, Pangolin, Itim, Mali, Charm, Sriracha, Playpen Sans, Dancing Script, Lobster, Pacifico |
| Mono, kỹ thuật | JetBrains Mono, IBM Plex Mono, Space Mono, Roboto Mono, Source Code Pro, Inconsolata, VT323, Chakra Petch, Tektur |

## Thay font không có tiếng Việt

| Font gốc (KHÔNG có tiếng Việt) | Thay bằng |
|---|---|
| Bebas Neue | Oswald 600/700 hoặc Anton |
| Archivo Black | Archivo 900 hoặc Be Vietnam Pro 900 |
| Syne | Unbounded hoặc Bricolage Grotesque 800 |
| Clash Display | Space Grotesk 700 hoặc Unbounded |
| Shrikhand | Lobster |
| Caveat, Caveat Brush | Patrick Hand, Pangolin hoặc Itim |
| Press Start 2P, Silkscreen, Pixelify Sans | VT323 (pixel) hoặc Tektur |
| Instrument Serif, DM Serif Display, Gloock, Young Serif, Zilla Slab (-> Roboto Slab) | Playfair Display hoặc Fraunces |
| Bodoni Moda | Libre Bodoni hoặc Playfair Display |
| Jost, DM Sans, Outfit, Sora, Rubik, Instrument Sans, Albert Sans | Be Vietnam Pro, Manrope hoặc Plus Jakarta Sans |
| DM Mono, Courier Prime | IBM Plex Mono hoặc Space Mono |
| Stardos Stencil | Big Shoulders Stencil Display hoặc Saira Stencil One |
| Bowlby One, Rammetto One, Righteous | Dela Gothic One, Paytone One hoặc Bungee |
| Libre Baskerville | Lora hoặc Libre Bodoni |
| Orbitron | Tektur hoặc Chakra Petch |
| MS Sans Serif (hệ thống) | Be Vietnam Pro 500 + VT323 |

**Lưu ý chữ in hoa:** tiếng Việt in hoa có dấu chồng cao (Ể, Ặ, Ỗ). Tiêu đề in hoa (nhất là Oswald, Anton, League Gothic) cần `line-height` tối thiểu 1.2 để dấu không chạm dòng trên.

**Lưu ý số kiểu cũ:** Playfair Display mặc định dùng số kiểu cũ (01 trông như O1). Số lớn nên thêm `font-variant-numeric: lining-nums`.
