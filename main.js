import './style.css';
import translationsData from './translations.json';
import productsData from './products.json';

// ===== Global State =====
let currentLang = 'en'; // Default language
let translations = translationsData;
let products = productsData;
let inquiryBasket = [];

// Fallback logic for languages
const langFallbacks = {
  'zh-TW': 'zh',
  'ja': 'en',
  'ko': 'en',
  'de': 'en',
  'fr': 'en',
  'es': 'en'
};

// ===== Initialize App =====
function init() {
  setupEventListeners();
  updateLanguage(currentLang);
  renderProducts();
  setupScrollAnimations();
  setupNavbarScroll();
}

// ===== Language Switching =====
function updateLanguage(lang) {
  currentLang = lang;

  // Update active language button in dropdown
  document.querySelectorAll('.lang-option').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  // Update current language display
  const currentLangDisplay = document.querySelector('.current-lang');
  if (currentLangDisplay) {
    const langNames = {
      'en': 'EN',
      'zh': '简',
      'zh-TW': '繁',
      'ja': 'JP',
      'ko': 'KR',
      'de': 'DE',
      'fr': 'FR',
      'es': 'ES'
    };
    currentLangDisplay.textContent = langNames[lang] || lang.toUpperCase();
  }

  // Update all i18n elements
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.dataset.i18n;
    const translation = getTranslation(key);

    if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
      element.placeholder = translation;
    } else {
      element.textContent = translation;
    }
  });

  // Update HTML lang attribute
  document.documentElement.lang = lang;

  // Re-render products with new language
  renderProducts();
}

function getTranslation(key) {
  const keys = key.split('.');
  let value = translations[currentLang];

  for (const k of keys) {
    value = value?.[k];
  }

  return value || key;
}

// ===== Render Products =====
function renderProducts(category = 'all') {
  const grid = document.getElementById('productsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  const filteredProducts = category === 'all'
    ? products
    : products.filter(p => p.category === category);

  // Animation delay
  let delay = 0;

  filteredProducts.forEach(product => {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.style.animationDelay = `${delay}ms`;
    delay += 50;

    // Get localized name with fallback
    let name = '';
    if (product.names) {
      name = product.names[currentLang] ||
        product.names[langFallbacks[currentLang]] ||
        product.names['en'] ||
        product.name;
    } else {
      name = product.name;
    }

    // Get localized specs with fallback
    let specs = [];
    if (product.specs && !Array.isArray(product.specs)) {
      // It's an object with language keys
      specs = product.specs[currentLang] ||
        product.specs[langFallbacks[currentLang]] ||
        product.specs['en'] ||
        [];
    } else if (Array.isArray(product.specs)) {
      // Legacy array format
      specs = product.specs;
    }

    // Certifications Badges
    let certBadges = '';
    if (product.certifications) {
      if (product.certifications.ce) certBadges += `<span class="cert-badge mini">CE</span>`;
      if (product.certifications.fcc) certBadges += `<span class="cert-badge mini">FCC</span>`;
      if (product.certifications.rohs) certBadges += `<span class="cert-badge mini">RoHS</span>`;
    }

    const addToInquiryText = translations[currentLang]?.product?.addToInquiry || 'Add to Inquiry';
    const oemText = translations[currentLang]?.product?.oem || 'OEM/ODM';
    const categoryText = translations[currentLang]?.categories?.[product.category] || product.category;
    const moqLabel = translations[currentLang]?.product?.moq || 'MOQ';
    const pcsText = translations[currentLang]?.product?.pcs || 'pcs';

    card.innerHTML = `
      <div class="product-image-container ${product.packagingImage ? 'has-packaging' : ''}">
        <img src="${product.image}" alt="${name}" class="product-image main-img" loading="lazy">
        ${product.packagingImage ? `<img src="${product.packagingImage}" alt="${name} Packaging" class="product-image packaging-img" loading="lazy">` : ''}
        <div class="product-overlay">
          <button class="btn-icon" onclick="addToInquiry('${product.id}')" title="${addToInquiryText}">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
            </svg>
          </button>
        </div>
        ${product.oem ? `<span class="badge-oem">${oemText}</span>` : ''}
      </div>
      <div class="product-info">
        <div class="product-category">${categoryText}</div>
        <h3 class="product-title">${name}</h3>
        <ul class="product-specs">
          ${specs.slice(0, 3).map(spec => `<li>${spec}</li>`).join('')}
        </ul>
        <div class="product-certifications-mini">
          ${certBadges}
        </div>
        <div class="product-footer">
          <span class="moq-label">${moqLabel}: ${product.moq} ${pcsText}</span>
        </div>
      </div>
    `;

    grid.appendChild(card);
  });

  // Add click handlers for "Add to Inquiry" buttons
  // Note: The onclick in HTML calls global addToInquiry, but we also want to support event listeners if needed
  // Since we used onclick attribute above, we need to make addToInquiry global or attach listeners here.
  // The original code used onclick in HTML string which requires the function to be on window.
  // Let's attach it to window to be safe for the inline onclick.
  window.addToInquiry = addToInquiry;
}

// ===== Inquiry Basket =====
function addToInquiry(productId) {
  if (!inquiryBasket.includes(productId)) {
    inquiryBasket.push(productId);
    updateBasketCount();
    showNotification('Product added to inquiry basket!');
  } else {
    showNotification('Product already in basket');
  }
}

function updateBasketCount() {
  const countElement = document.querySelector('.basket-count');
  if (countElement) {
    countElement.textContent = inquiryBasket.length;
  }
}

function showNotification(message) {
  // Simple notification
  const notification = document.createElement('div');
  notification.style.cssText = `
    position: fixed;
    top: 100px;
    right: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem 2rem;
    border-radius: 50px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    z-index: 10000;
    animation: slideInRight 0.3s ease-out;
  `;
  notification.textContent = message;
  document.body.appendChild(notification);

  setTimeout(() => {
    notification.style.animation = 'slideOutRight 0.3s ease-out';
    setTimeout(() => notification.remove(), 300);
  }, 3000);
}

// ===== Event Listeners =====
function setupEventListeners() {
  // Language switcher
  document.querySelectorAll('.lang-option, .lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      updateLanguage(btn.dataset.lang);
      // Close dropdown menu after selection
      document.querySelector('.lang-menu')?.classList.remove('active');
    });
  });

  // Toggle language dropdown
  document.querySelector('.lang-toggle')?.addEventListener('click', () => {
    document.querySelector('.lang-menu')?.classList.toggle('active');
  });

  // Category filters
  document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderProducts(btn.dataset.category);
    });
  });

  // Mobile menu toggle
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileMenuToggle && navMenu) {
    mobileMenuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Smooth scroll for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offsetTop = target.offsetTop - 80;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });

  // Inquiry form submission
  const inquiryForm = document.getElementById('inquiryForm');
  if (inquiryForm) {
    inquiryForm.addEventListener('submit', handleFormSubmit);
  }

  // Catalog download
  const downloadBtn = document.getElementById('downloadCatalog');
  if (downloadBtn) {
    downloadBtn.addEventListener('click', handleCatalogDownload);
  }

  // Inquiry basket click
  const basketFloat = document.getElementById('inquiryBasket');
  if (basketFloat) {
    basketFloat.addEventListener('click', showInquiryBasket);
  }

  // CTA buttons
  document.querySelectorAll('.btn-primary, .btn-secondary, .nav-cta').forEach(btn => {
    const text = btn.textContent;
    if (text.includes('Quote') || text.includes('报价') || text.includes('Cotización') || text.includes('Angebot')) {
      btn.addEventListener('click', () => {
        document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
      });
    }
    if (text.includes('Explore') || text.includes('浏览') || text.includes('Explorar') || text.includes('Erkunden')) {
      btn.addEventListener('click', () => {
        document.getElementById('products')?.scrollIntoView({ behavior: 'smooth' });
      });
    }
  });
}

// ===== Form Handling =====
async function handleFormSubmit(e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  // Add inquiry basket products
  if (inquiryBasket.length > 0) {
    const productNames = inquiryBasket.map(id => {
      const product = products.find(p => p.id === id);
      return product ? product.name : id;
    }).join(', ');
    data.inquiryProducts = productNames;
  }

  // Show loading state
  const submitBtn = e.target.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  submitBtn.textContent = 'Sending...';
  submitBtn.disabled = true;

  try {
    // Here you would send to your backend or form service
    // For now, we'll simulate a successful submission
    await new Promise(resolve => setTimeout(resolve, 1500));

    showNotification('✅ Inquiry sent successfully! We will contact you soon.');
    e.target.reset();
    inquiryBasket = [];
    updateBasketCount();
  } catch (error) {
    showNotification('❌ Failed to send inquiry. Please try again.');
  } finally {
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
  }
}

// ===== Catalog Download =====
function handleCatalogDownload() {
  // Show email capture modal
  const modal = document.createElement('div');
  modal.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    animation: fadeIn 0.3s ease-out;
  `;

  modal.innerHTML = `
    <div style="
      background: white;
      padding: 3rem;
      border-radius: 2rem;
      max-width: 500px;
      width: 90%;
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
      animation: slideInUp 0.3s ease-out;
    ">
      <h2 style="margin-bottom: 1rem; font-size: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Download 2025 Catalog
      </h2>
      <p style="margin-bottom: 2rem; color: #64748b;">
        Enter your email to receive our latest product catalog and price list.
      </p>
      <form id="catalogForm">
        <input 
          type="email" 
          name="email" 
          placeholder="Your email address" 
          required
          style="
            width: 100%;
            padding: 1rem;
            border: 2px solid #e2e8f0;
            border-radius: 1rem;
            font-size: 1rem;
            margin-bottom: 1rem;
          "
        >
        <div style="display: flex; gap: 1rem;">
          <button 
            type="submit"
            style="
              flex: 1;
              padding: 1rem;
              background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
              color: white;
              border: none;
              border-radius: 50px;
              font-weight: 600;
              cursor: pointer;
            "
          >
            Download PDF
          </button>
          <button 
            type="button"
            class="close-modal"
            style="
              padding: 1rem 2rem;
              background: #f1f5f9;
              color: #64748b;
              border: none;
              border-radius: 50px;
              font-weight: 600;
              cursor: pointer;
            "
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  `;

  document.body.appendChild(modal);

  // Close modal
  modal.querySelector('.close-modal').addEventListener('click', () => {
    modal.style.animation = 'fadeOut 0.3s ease-out';
    setTimeout(() => modal.remove(), 300);
  });

  // Handle form submission
  modal.querySelector('#catalogForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = e.target.email.value;

    // Here you would send the email to your backend
    await new Promise(resolve => setTimeout(resolve, 1000));

    showNotification('✅ Catalog sent to ' + email);
    modal.style.animation = 'fadeOut 0.3s ease-out';
    setTimeout(() => modal.remove(), 300);

    // Trigger download
    // window.open('/catalog-2025.pdf', '_blank');
  });
}

// ===== Inquiry Basket Modal =====
function showInquiryBasket() {
  if (inquiryBasket.length === 0) {
    showNotification('Your inquiry basket is empty');
    return;
  }

  const basketProducts = inquiryBasket.map(id => {
    return products.find(p => p.id === id);
  }).filter(Boolean);

  const modal = document.createElement('div');
  modal.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    animation: fadeIn 0.3s ease-out;
  `;

  modal.innerHTML = `
    <div style="
      background: white;
      padding: 3rem;
      border-radius: 2rem;
      max-width: 600px;
      width: 90%;
      max-height: 80vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    ">
      <h2 style="margin-bottom: 2rem; font-size: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Inquiry Basket (${inquiryBasket.length})
      </h2>
      <div style="margin-bottom: 2rem;">
        ${basketProducts.map(product => `
          <div style="
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 1rem;
            margin-bottom: 1rem;
          ">
            <img src="${product.image}" alt="${product.name}" style="width: 60px; height: 60px; object-fit: contain; border-radius: 0.5rem;">
            <div style="flex: 1;">
              <h4 style="margin-bottom: 0.25rem;">${product.name}</h4>
              <p style="font-size: 0.875rem; color: #64748b;">MOQ: ${product.moq} pcs</p>
            </div>
            <button 
              class="remove-from-basket" 
              data-product-id="${product.id}"
              style="
                padding: 0.5rem 1rem;
                background: #fee2e2;
                color: #dc2626;
                border: none;
                border-radius: 50px;
                cursor: pointer;
                font-weight: 600;
              "
            >
              Remove
            </button>
          </div>
        `).join('')}
      </div>
      <div style="display: flex; gap: 1rem;">
        <button 
          class="send-inquiry"
          style="
            flex: 1;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            cursor: pointer;
          "
        >
          Send Inquiry
        </button>
        <button 
          class="close-modal"
          style="
            padding: 1rem 2rem;
            background: #f1f5f9;
            color: #64748b;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            cursor: pointer;
          "
        >
          Close
        </button>
      </div>
    </div>
  `;

  document.body.appendChild(modal);

  // Close modal
  modal.querySelector('.close-modal').addEventListener('click', () => {
    modal.style.animation = 'fadeOut 0.3s ease-out';
    setTimeout(() => modal.remove(), 300);
  });

  // Remove from basket
  modal.querySelectorAll('.remove-from-basket').forEach(btn => {
    btn.addEventListener('click', () => {
      inquiryBasket = inquiryBasket.filter(id => id !== btn.dataset.productId);
      updateBasketCount();
      modal.remove();
      if (inquiryBasket.length > 0) {
        showInquiryBasket();
      } else {
        showNotification('Basket is now empty');
      }
    });
  });

  // Send inquiry
  modal.querySelector('.send-inquiry').addEventListener('click', () => {
    modal.remove();
    document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });

    // Pre-fill products field
    const productsField = document.getElementById('products');
    if (productsField) {
      productsField.value = basketProducts.map(p => p.name).join(', ');
    }
  });
}

// ===== Scroll Animations =====
function setupScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
      }
    });
  }, observerOptions);

  // Observe all sections
  document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
  });
}

// ===== Navbar Scroll Effect =====
function setupNavbarScroll() {
  const navbar = document.querySelector('.navbar');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
      navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
    } else {
      navbar.style.boxShadow = '0 1px 2px 0 rgb(0 0 0 / 0.05)';
    }

    lastScroll = currentScroll;
  });
}

// ===== Initialize on DOM Load =====
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
