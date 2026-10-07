# Meta Icons

Instagram 與 Threads 的圖示收藏，共 **2,055 個**，含 SVG 向量與 @3x PNG。

做 App 或網頁時常常需要對照 Instagram、Threads 的介面圖示，但 Meta 沒有公開的圖示庫，官方設計系統（IGDS）也不對外。這個倉庫把散落在網頁資源與 App 資源包裡的圖示整理成可以搜尋、可以直接取用的形式。

## 快速預覽

開啟 [`index.html`](index.html) 就能瀏覽全部圖示，支援搜尋與一鍵複製路徑。不需要安裝任何東西，直接用瀏覽器打開即可。

| 總覽圖 | 內容 |
|---|---|
| [previews/instagram-overview.png](previews/instagram-overview.png) | Instagram 網頁版圖示總覽 |
| [previews/threads-overview.png](previews/threads-overview.png) | Threads 網頁版圖示總覽 |
| [previews/vector-comparison.png](previews/vector-comparison.png) | 向量版與原圖的對照 |

## 內容

```
icons/
├── instagram/
│   ├── web/        322 個 SVG   網頁版圖示（IGDS、FBNucleus 系列）
│   │   └── _broken/ 13 個       無法正常顯示的，保留備查
│   ├── ios/       1483 個 PNG   iOS 版圖示，全部 @3x
│   └── vector/      24 個 SVG   向量化版本（部分 iOS 圖示與筆刷工具）
└── threads/
    └── web/        226 個 SVG   Threads 網頁版圖示（內部代號 Barcelona）
        └── _broken/ 11 個
```

### 命名規則

檔名沿用 Meta 內部的命名，看得懂規則就很好找：

- **`IGDS...`** — Instagram Design System，網頁版主要系列
- **`Barcelona...`** — Threads 的內部代號
- **`ig_icon_<名稱>_<樣式>_<尺寸>`** — iOS 版，例如 `ig_icon_heart_filled_24@3x.png`
  - 樣式：`outline`（線條）、`filled`（實心）
  - 尺寸：10 / 12 / 16 / 18 / 20 / 24 / 44 等（單位為點，實際像素為三倍）

搜尋時直接用英文關鍵字，例如 `heart`、`camera`、`arrow`、`chevron`、`settings`。

## 使用方式

SVG 可以直接內嵌到網頁或丟進 Figma；PNG 是 @3x，用於 iOS 專案時放進 Asset Catalog 即可。

```html
<img src="icons/instagram/web/IGDSHeartPanoOutlineIcon.svg" width="24" alt="">
```

深色背景下，單色 SVG 可以用 CSS 直接反轉：

```css
.icon-dark { filter: invert(1); }
```

## 來源與授權

**這些圖示的著作權屬於 Meta Platforms, Inc.**，擷取自 Instagram 與 Threads 的公開網頁資源及 iOS App 資源包（版本 436）。本倉庫僅作為設計參考與研究用途的整理，不主張任何權利，也不隸屬於 Meta 或獲得其授權。

Instagram、Threads、WhatsApp、Meta 及其標誌為 Meta Platforms, Inc. 的註冊商標。

商業使用前請自行評估風險，或依照 [Meta 品牌使用規範](https://about.meta.com/brand/resources/) 取得授權。若 Meta 要求移除，本倉庫會配合下架。

整理與向量化的部分由 [@hongyinull](https://github.com/hongyinull) 完成。
