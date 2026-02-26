import re

path = 'c:/Users/Damian/Desktop/horizont/horizont.odoo/doc/vendedores/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<html lang="es" class="dark">', '<html lang="es">')

css_find = '''        .bg-glass {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }'''
css_replace = '''        .bg-glass {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .dark .bg-glass {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }'''
html = html.replace(css_find, css_replace)

body_find = 'class="font-body bg-background-dark text-slate-300 antialiased min-h-screen relative overflow-x-hidden selection:bg-secondary selection:text-slate-900 pb-20"'
body_replace = 'class="font-body bg-slate-50 dark:bg-background-dark text-slate-700 dark:text-slate-300 antialiased min-h-screen relative overflow-x-hidden selection:bg-primary selection:text-white dark:selection:bg-secondary dark:selection:text-slate-900 pb-20 transition-colors duration-300"'
html = html.replace(body_find, body_replace)

html = html.replace('bg-blue-900/20', 'bg-blue-500/10 dark:bg-blue-900/20')
html = html.replace('bg-lime-900/10', 'bg-lime-500/10 dark:bg-lime-900/10')

header_find = '''    <header class="sticky top-0 z-50 bg-slate-900/80 backdrop-blur-md border-b border-white/5">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-white rounded-md flex items-center justify-center">
                    <span class="material-icons-round text-black text-xl">grid_view</span>
                </div>
                <span class="font-display font-bold text-xl tracking-tight text-white">horizont<span
                        class="text-secondary">.</span></span>
            </div>
            <div class="text-xs font-bold tracking-widest text-slate-400 uppercase flex items-center gap-1">
                <span class="material-icons-round text-[14px]">lock</span>
                Acceso Restringido
            </div>
        </div>
    </header>'''
header_replace = '''    <header class="sticky top-0 z-50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-gray-200 dark:border-white/5 transition-colors">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-black dark:bg-white rounded-md flex items-center justify-center transition-colors">
                    <span class="material-icons-round text-white dark:text-black text-xl">grid_view</span>
                </div>
                <span class="font-display font-bold text-xl tracking-tight text-slate-900 dark:text-white">horizont<span
                        class="text-primary dark:text-secondary">.</span></span>
            </div>
            <div class="flex items-center gap-4">
                <div class="text-[10px] md:text-xs font-bold tracking-widest text-slate-500 dark:text-slate-400 border border-slate-200 dark:border-slate-800 px-3 py-1 rounded-full uppercase flex items-center gap-1 bg-slate-100 dark:bg-transparent transition-colors">
                    <span class="material-icons-round text-[14px]">lock</span>
                    Acceso Restringido
                </div>
                <!-- Theme Toggle Button -->
                <button
                    class="p-2 text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white transition-colors"
                    id="theme-toggle" aria-label="Toggle theme">
                    <span class="material-icons-round text-xl dark:hidden">dark_mode</span>
                    <span class="material-icons-round text-xl hidden dark:block">light_mode</span>
                </button>
            </div>
        </div>
    </header>'''
html = html.replace(header_find, header_replace)

# Regular Expressions
html = re.sub(r'\btext-white\b', r'text-slate-900 dark:text-white', html)
html = html.replace('bg-primary text-slate-900 dark:text-white', 'bg-primary text-white')

html = re.sub(r'\btext-slate-400\b', r'text-slate-500 dark:text-slate-400', html)
html = re.sub(r'\btext-slate-300\b', r'text-slate-700 dark:text-slate-300', html)

html = re.sub(r'\bbg-slate-800/50\b', r'bg-white/80 dark:bg-slate-800/50', html)
html = re.sub(r'\bborder-slate-700/50\b', r'border-slate-200 dark:border-slate-700/50', html)

html = re.sub(r'\bbg-slate-900/50\b', r'bg-slate-100 dark:bg-slate-900/50', html)
html = re.sub(r'\bbg-slate-900/90\b', r'bg-white/90 dark:bg-slate-900/90', html)
html = re.sub(r'\bbg-slate-900(?![/\-\w])', r'bg-slate-100 dark:bg-slate-900', html)

html = re.sub(r'\bbg-slate-800/80\b', r'bg-white/80 dark:bg-slate-800/80', html)
html = re.sub(r'\bbg-slate-800(?![/\-\w])', r'bg-white dark:bg-slate-800', html)

html = re.sub(r'\bborder-slate-700(?![/\-\w])', r'border-slate-200 dark:border-slate-700', html)
html = re.sub(r'\bborder-slate-800(?![/\-\w])', r'border-slate-200 dark:border-slate-800', html)

html = re.sub(r'\bborder-white/10\b', r'border-slate-200 dark:border-white/10', html)
html = re.sub(r'\bborder-white/5\b', r'border-slate-200 dark:border-white/5', html)

html = html.replace('from-indigo-900/40 to-slate-900/40', 'from-indigo-50 dark:from-indigo-900/40 to-white dark:to-slate-900/40')
html = html.replace('from-indigo-900/60 to-slate-900', 'from-blue-50 dark:from-indigo-900/60 to-white dark:to-slate-900')
html = html.replace('from-slate-900 to-indigo-900/30', 'from-white dark:from-slate-900 to-indigo-50 dark:to-indigo-900/30')

html = re.sub(r'\bbg-slate-950\b', r'bg-slate-200 dark:bg-slate-950', html)

script_find = '</body>'
script_replace = '''
    <script>
        const themeToggleBtn = document.getElementById('theme-toggle');
        const htmlElement = document.documentElement;
        
        // Check for saved user preference
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            htmlElement.classList.add('dark');
        } else {
            htmlElement.classList.remove('dark');
        }
        
        if (themeToggleBtn) {
            themeToggleBtn.addEventListener('click', function () {
                if (htmlElement.classList.contains('dark')) {
                    htmlElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    htmlElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            });
        }
    </script>
</body>
'''
if '<script>' not in html:
    html = html.replace(script_find, script_replace)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
