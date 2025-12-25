# 🚀 快速启动指南

## 欢迎使用 MEWPOW 外贸独立站！

这是一个为您量身打造的高端B2B网站。本指南将帮助您在5分钟内了解如何使用和维护网站。

---

## 📋 第一步：查看网站

网站已经在本地运行！

**访问地址**: http://localhost:5173

**功能演示**:
- ✅ 点击右上角切换语言（EN/中文/ES/DE）
- ✅ 点击产品分类按钮筛选产品
- ✅ 点击"Add to Inquiry"添加产品到询价篮
- ✅ 滚动查看所有模块
- ✅ 填写联系表单测试

---

## 📝 第二步：更新基本信息

### 1. 更新联系方式（5分钟）

打开 `index.html` 文件，搜索并替换：

```html
<!-- 邮箱 -->
sales@mewpow.com → 你的邮箱

<!-- WhatsApp -->
wa.me/86138xxxxxxxx → wa.me/你的号码

<!-- 地址 -->
Shenzhen, Guangdong, China → 你的地址
```

### 2. 更新公司介绍（5分钟）

打开 `translations.json` 文件，修改：

```json
"about": {
  "desc1": "你的公司介绍第一段",
  "desc2": "你的公司介绍第二段"
}
```

---

## 🖼️ 第三步：管理产品

### 使用可视化工具（推荐）

1. 在浏览器打开: `product-manager.html`
2. 下载Excel模板
3. 填写产品信息
4. 上传Excel文件
5. 下载生成的 `products.json`
6. 替换原文件

**产品类别代码**:
- humidifier (加湿器)
- hairdryer (吹风机)
- heater (取暖器)
- fan (风扇)
- purifier (空气净化器)

---

## 🌐 第四步：部署上线

### 最简单的方法：Netlify（免费）

1. **注册账号**
   - 访问 https://www.netlify.com
   - 使用GitHub账号登录

2. **上传代码**
   ```bash
   # 在website文件夹中执行
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. **推送到GitHub**
   - 在GitHub创建新仓库
   - 按提示推送代码

4. **连接Netlify**
   - 在Netlify点击 "Add new site"
   - 选择GitHub仓库
   - 点击 "Deploy"

5. **完成！**
   - 获得免费域名: `你的名字.netlify.app`
   - 自动HTTPS
   - 全球CDN加速

**详细步骤**: 查看 `DEPLOYMENT.md`

---

## 📧 第五步：配置表单

### 使用Formspree（推荐）

1. **注册**
   - 访问 https://formspree.io
   - 免费注册账号

2. **创建表单**
   - 点击 "New Form"
   - 获取表单ID（例如：`abc123`）

3. **配置代码**
   
   打开 `main.js`，找到 `handleFormSubmit` 函数，替换为：

   ```javascript
   async function handleFormSubmit(e) {
     e.preventDefault();
     const formData = new FormData(e.target);
     
     const response = await fetch('https://formspree.io/f/你的表单ID', {
       method: 'POST',
       body: formData,
       headers: { 'Accept': 'application/json' }
     });
     
     if (response.ok) {
       showNotification('✅ Inquiry sent successfully!');
       e.target.reset();
     }
   }
   ```

4. **测试**
   - 提交表单
   - 检查邮箱是否收到

---

## 🎨 第六步：自定义样式（可选）

### 更改颜色主题

打开 `style.css`，修改顶部的颜色变量：

```css
:root {
  /* 主色调 - 改成你喜欢的颜色 */
  --color-primary: #2563eb;
  
  /* 渐变色 */
  --gradient-primary: linear-gradient(135deg, #你的颜色1 0%, #你的颜色2 100%);
}
```

### 更换Logo

替换 `public/logo.svg` 为你的Logo文件。

---

## 📚 重要文档

| 文档 | 用途 | 适合人群 |
|------|------|----------|
| `README.md` | 技术说明 | 开发人员 |
| `DEPLOYMENT.md` | 部署指南 | 技术人员 |
| `MAINTENANCE.md` | 维护手册 | **所有人** ⭐ |
| `PROJECT_SUMMARY.md` | 项目总结 | 管理层 |

**推荐先看**: `MAINTENANCE.md`（日常维护手册）

---

## ✅ 检查清单

上线前请确认：

- [ ] 已更新联系信息（邮箱、WhatsApp、地址）
- [ ] 已更新公司介绍
- [ ] 已配置表单服务
- [ ] 已测试所有语言版本
- [ ] 已测试表单提交
- [ ] 已测试移动端显示
- [ ] 已准备域名（可选）

---

## 🆘 遇到问题？

### 常见问题

**Q: 图片不显示？**  
A: 检查图片是否在 `public/products/` 文件夹中。

**Q: 表单提交失败？**  
A: 确保已配置Formspree或Web3Forms。

**Q: 多语言不生效？**  
A: 检查 `translations.json` 格式是否正确。

**Q: 网站修改后没变化？**  
A: 按 Ctrl+F5 (Windows) 或 Cmd+Shift+R (Mac) 强制刷新。

### 获取帮助

1. 查看 `MAINTENANCE.md` 维护手册
2. 查看浏览器控制台错误（按F12）
3. 联系技术支持

---

## 🎯 下一步建议

### 本周完成
1. ✅ 更新所有联系信息
2. ✅ 配置表单服务
3. ✅ 部署到Netlify
4. ✅ 测试所有功能

### 本月完成
1. 📝 准备产品目录PDF
2. 🌐 配置自定义域名
3. 📊 添加Google Analytics
4. 🎥 上传工厂视频

### 持续优化
1. 定期更新产品信息
2. 收集客户反馈
3. 优化产品图片
4. 添加客户案例

---

## 💡 专业提示

1. **备份很重要**
   - 定期备份 `products.json`
   - 备份产品图片
   - 使用Git版本控制

2. **定期测试**
   - 每周测试表单
   - 检查所有链接
   - 测试移动端

3. **保持更新**
   - 定期更新产品
   - 及时回复询盘
   - 更新公司动态

---

## 🎉 恭喜！

您已经掌握了网站的基本使用方法！

**记住**：
- 📖 遇到问题先查看 `MAINTENANCE.md`
- 🔄 每次修改后要保存并刷新浏览器
- 💾 重要文件记得备份
- 📧 及时回复客户询盘

**祝您生意兴隆！** 🚀

---

**快速链接**:
- 本地网站: http://localhost:5173
- 产品管理: http://localhost:5173/product-manager.html
- Netlify: https://www.netlify.com
- Formspree: https://formspree.io
