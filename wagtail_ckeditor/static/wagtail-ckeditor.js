import * as CK from './ckeditor5/ckeditor5/ckeditor5.js';  // or wherever your build lives

(function() {
  const config = window.ckeditorConfig || {};
  const pluginNames = window.ckeditorPluginNames || [];

  // Convert the list of names into constructor references
  const plugins = pluginNames.map(name => CK[name]);

  function init(el) {
    if (el._ckeditorInitialized) return;
    el._ckeditorInitialized = true;

    CK.ClassicEditor
      .create(el, {
        ...config,
        plugins,
      })
      .catch(err => console.error("CKEditor init failed:", err));
  }

  // On load
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("textarea.ckeditor5").forEach(init);
  });

  // Watch for dynamically added StreamField blocks
  new MutationObserver(muts => {
    muts.forEach(m => {
      m.addedNodes.forEach(node => {
        if (node.querySelectorAll) {
          node.querySelectorAll("textarea.ckeditor5").forEach(init);
        }
      });
    });
  }).observe(document.body, { childList: true, subtree: true });
})();