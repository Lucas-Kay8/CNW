document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const container = document.querySelector('.ppt-container');
    let currentStep = 0;

    // 1. 初始化导航 UI
    const navDots = document.createElement('div');
    navDots.className = 'ppt-nav-dots';
    const progressBar = document.createElement('div');
    progressBar.className = 'ppt-progress';
    document.body.appendChild(navDots);
    document.body.appendChild(progressBar);

    slides.forEach((_, i) => {
        const dot = document.createElement('div');
        dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
        dot.onclick = () => goToSlide(i);
        navDots.appendChild(dot);
    });

    // 2. 翻页核心逻辑
    function goToSlide(index) {
        if (index < 0 || index >= slides.length) return;
        
        slides[currentStep].classList.remove('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.remove('active');
        
        currentStep = index;
        
        slides[currentStep].classList.add('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.add('active');
        progressBar.style.width = `${((currentStep + 1) / slides.length) * 100}%`;
        
        // 滚动到指定 slide
        slides[index].scrollIntoView({ behavior: 'smooth' });
    }

    // 3. 键盘事件监听
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            goToSlide(currentStep + 1);
        } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft' || e.key === 'Backspace') {
            e.preventDefault();
            goToSlide(currentStep - 1);
        }
    });

    // 4. Scroll Spy (同步滚动与动画状态)
    const observerOptions = {
        threshold: 0.6
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const index = Array.from(slides).indexOf(entry.target);
                if (index !== -1 && index !== currentStep) {
                    slides[currentStep].classList.remove('active');
                    document.querySelectorAll('.nav-dot')[currentStep].classList.remove('active');
                    
                    currentStep = index;
                    
                    entry.target.classList.add('active');
                    document.querySelectorAll('.nav-dot')[currentStep].classList.add('active');
                    progressBar.style.width = `${((currentStep + 1) / slides.length) * 100}%`;
                }
            }
        });
    }, observerOptions);

    slides.forEach(slide => observer.observe(slide));

    // 5. 初始化第一页
    slides[0].classList.add('active');
});
