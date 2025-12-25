# 🚀 MEWPOW网站快速部署指南

## 📋 部署前检查清单

在部署之前，请确保完成以下步骤：

- [ ] 更新产品数据（products.json）
- [ ] 替换产品图片（public/products/）
- [ ] 上传工厂视频（public/videos/factory.mp4）或使用静态图片
- [ ] 更新联系信息（index.html中的邮箱、WhatsApp、地址）
- [ ] 准备产品目录PDF（可选）
- [ ] 测试所有语言版本

## 🌐 方式一：Netlify部署（推荐）

### 步骤1：准备Git仓库

```bash
cd website
git init
git add .
git commit -m "Initial commit"
```

### 步骤2：推送到GitHub

1. 在GitHub创建新仓库（例如：mewpow-website）
2. 推送代码：

```bash
git remote add origin https://github.com/你的用户名/mewpow-website.git
git branch -M main
git push -u origin main
```

### 步骤3：连接Netlify

1. 访问 https://www.netlify.com
2. 点击 "Add new site" → "Import an existing project"
3. 选择 GitHub，授权并选择你的仓库
4. 构建设置：
   - Build command: `npm run build`
   - Publish directory: `dist`
5. 点击 "Deploy site"

### 步骤4：配置自定义域名

1. 在Netlify项目设置中，点击 "Domain settings"
2. 点击 "Add custom domain"
3. 输入你的域名（例如：www.mewpow.com）
4. 按照提示配置DNS记录

**DNS配置示例：**
```
类型    名称    值
A       @       75.2.60.5
CNAME   www     你的netlify域名.netlify.app
```

### 步骤5：启用HTTPS

Netlify会自动为你的域名配置免费SSL证书（Let's Encrypt）。

---

## 🔷 方式二：Vercel部署

### 使用Vercel CLI

```bash
# 安装Vercel CLI
npm i -g vercel

# 登录
vercel login

# 部署
cd website
vercel

# 生产部署
vercel --prod
```

### 使用Vercel网页界面

1. 访问 https://vercel.com
2. 导入GitHub仓库
3. 框架预设选择 "Vite"
4. 点击 "Deploy"

---

## 📧 表单集成配置

### 使用Formspree（推荐）

1. 注册 https://formspree.io
2. 创建新表单，获取表单ID
3. 在 `main.js` 的 `handleFormSubmit` 函数中添加：

```javascript
async function handleFormSubmit(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  
  try {
    const response = await fetch('https://formspree.io/f/你的表单ID', {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    });
    
    if (response.ok) {
      showNotification('✅ Inquiry sent successfully!');
      e.target.reset();
    }
  } catch (error) {
    showNotification('❌ Failed to send inquiry.');
  }
}
```

### 使用Web3Forms

1. 访问 https://web3forms.com
2. 获取Access Key
3. 在表单中添加隐藏字段：

```html
<input type="hidden" name="access_key" value="你的Access Key">
```

---

## 📊 Google Analytics集成

在 `index.html` 的 `<head>` 中添加：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-你的ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-你的ID');
</script>
```

---

## 🔍 SEO优化清单

### 1. 更新Meta标签

在 `index.html` 中自定义：

```html
<meta name="description" content="你的描述">
<meta name="keywords" content="关键词1, 关键词2, 关键词3">
<meta property="og:title" content="MEWPOW - Premium Small Appliance Manufacturer">
<meta property="og:description" content="你的描述">
<meta property="og:image" content="https://你的域名/og-image.jpg">
```

### 2. 创建sitemap.xml

在 `public/` 目录创建 `sitemap.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://你的域名/</loc>
    <lastmod>2025-01-01</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

### 3. 创建robots.txt

在 `public/` 目录创建 `robots.txt`：

```
User-agent: *
Allow: /
Sitemap: https://你的域名/sitemap.xml
```

---

## 📱 WhatsApp配置

在 `index.html` 中找到WhatsApp链接，更新为你的号码：

```html
<a href="https://wa.me/8613812345678?text=Hi,%20I%20am%20interested%20in%20your%20appliances..." 
   class="whatsapp-float">
```

**格式说明：**
- 国家代码：86（中国）
- 手机号：13812345678（去掉开头的0）
- 完整格式：8613812345678

---

## 🎨 品牌定制

### 更新Logo

替换 `public/logo.svg` 为你的Logo文件。

### 更新颜色主题

在 `style.css` 的 `:root` 中修改：

```css
:root {
  --color-primary: #你的主色;
  --gradient-primary: linear-gradient(135deg, #颜色1 0%, #颜色2 100%);
}
```

---

## 🔄 持续维护

### 更新产品

1. 打开 `product-manager.html`（在浏览器中）
2. 上传Excel文件或手动编辑
3. 下载生成的 `products.json`
4. 替换网站中的 `products.json`
5. 提交并推送到Git仓库

### 添加新产品图片

1. 将图片放入 `public/products/[类别]/`
2. 在 `products.json` 中添加产品信息
3. 提交并推送

### 更新翻译

编辑 `translations.json`，添加或修改文本。

---

## 🐛 常见问题

### Q: 图片不显示？
A: 检查图片路径是否正确，确保图片在 `public/` 目录中。

### Q: 表单提交失败？
A: 确保已配置表单服务（Formspree/Web3Forms）。

### Q: 多语言不生效？
A: 检查 `translations.json` 格式是否正确，确保所有语言都有对应翻译。

### Q: 视频不播放？
A: 确保视频格式为MP4 (H.264)，或使用静态图片替代。

### Q: 部署后样式错乱？
A: 运行 `npm run build` 测试生产构建，检查控制台错误。

---

## 📞 技术支持

如遇到问题，请检查：
1. 浏览器控制台错误信息
2. Netlify/Vercel部署日志
3. 网络请求是否成功

---

## ✅ 部署成功检查

部署完成后，请验证：

- [ ] 网站可以正常访问
- [ ] 所有图片正常加载
- [ ] 四种语言切换正常
- [ ] 产品筛选功能正常
- [ ] 表单可以提交
- [ ] WhatsApp链接可以打开
- [ ] 移动端显示正常
- [ ] HTTPS证书有效

---

🎉 **恭喜！你的外贸独立站已经成功上线！**
