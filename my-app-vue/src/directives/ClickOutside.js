export const ClickOutside = {
    beforeMount(el, binding, vnode) {
        el.event = function (event) {
            if (!(el === event.target || el.contains(event.target))) {
                binding.value();
            }
        };
        document.body.addEventListener('click', el.event);
    },
    unmounted(el) {
        document.body.removeEventListener('click', el.event);
    }
};
