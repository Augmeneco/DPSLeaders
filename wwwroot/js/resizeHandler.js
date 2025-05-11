let timeoutId;
window.screenResize = {
    listenForResize: (dotNetHelper) => {
        const handler = () => {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                dotNetHelper.invokeMethodAsync('UpdateScreenSize', window.innerWidth, window.innerHeight);
            }, 200);
        };
        handler();
        window.addEventListener('resize', handler);
        return handler.name;
    },
    removeResizeListener: (handlerName) => {
        window.removeEventListener('resize', window[handlerName]);
    }
};