document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const container = document.querySelector('.ppt-container');
    // 1. 初始化导航与锚点检测
    function getHashSlide() {
        const hash = window.location.hash.replace('#', '');
        const index = parseInt(hash) - 1;
        return (isNaN(index) || index < 0 || index >= slides.length) ? 0 : index;
    }

    let currentStep = getHashSlide();
    let isNavigating = false; // 防止 hashchange 与 goToSlide 循环触发

    const navDots = document.createElement('div');
    navDots.className = 'ppt-nav-dots';
    const progressBar = document.createElement('div');
    progressBar.className = 'ppt-progress';
    document.body.appendChild(navDots);
    document.body.appendChild(progressBar);

    slides.forEach((_, i) => {
        const dot = document.createElement('div');
        dot.className = 'nav-dot' + (i === currentStep ? ' active' : '');
        dot.onclick = () => goToSlide(i);
        navDots.appendChild(dot);
    });

    // 2. 翻页核心逻辑
    function goToSlide(index, updateHash = true) {
        if (index < 0 || index >= slides.length || isNavigating) return;
        
        isNavigating = true;
        
        slides[currentStep].classList.remove('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.remove('active');
        
        currentStep = index;
        
        slides[currentStep].classList.add('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.add('active');
        progressBar.style.width = `${((currentStep + 1) / slides.length) * 100}%`;
        
        // 滚动到指定 slide
        slides[index].scrollIntoView({ behavior: 'smooth' });

        // 更新 URL Hash
        if (updateHash) {
            window.location.hash = `#${index + 1}`;
        }

        // 延迟解锁，等待滚动完成
        setTimeout(() => { isNavigating = false; }, 500);
    }

    // 3. 键盘与同步事件
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            goToSlide(currentStep + 1);
        } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft' || e.key === 'Backspace') {
            e.preventDefault();
            goToSlide(currentStep - 1);
        }
    });

    window.addEventListener('hashchange', () => {
        const index = getHashSlide();
        if (index !== currentStep && !isNavigating) {
            goToSlide(index, false);
        }
    });

    // 4. Scroll Spy
    const observerOptions = { threshold: 0.6 };
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !isNavigating) {
                const index = Array.from(slides).indexOf(entry.target);
                if (index !== -1 && index !== currentStep) {
                    goToSlide(index, true);
                }
            }
        });
    }, observerOptions);

    slides.forEach(slide => observer.observe(slide));

    // 5. 初始跳转
    if (currentStep !== 0) {
        goToSlide(currentStep, false);
    } else {
        slides[0].classList.add('active');
        if (!window.location.hash) {
            history.replaceState(null, null, `#1`);
        }
    }
});
