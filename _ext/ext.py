import os
import subprocess
from docutils import nodes
from docutils.parsers.rst import Directive
from tutorials import tutorials
import sphinx_material

class Tutorials(Directive):

    def run(self):
        output = list()
        # General text
        intro = f"""
<p>
<b>viskex</b> is accompanied by a few tutorials, that can be run on JupyterLab through a local installation of the library, or on cloud computing platforms such as Google Colab and Kaggle.
</p>
"""
        output.append(nodes.raw(text=intro, format="html"))
        # Tutorials
        for num in tutorials.keys():
            data = tutorials[num]
            steps = data["steps"]
            buttons = ""
            for step_description in steps:
                step_files = steps[step_description]
                if len(step_files) == 1:
                    buttons += self._button(step_description, step_files)
                else:
                    buttons += self._dropdown(step_description, step_files)

            card_num = self._card(
                num=num,
                title=data["title"],
                description=data["description"],
                buttons=buttons
            )
            output.append(nodes.raw(text=card_num, format="html"))
        return output

    @staticmethod
    def _card(num, title, description, buttons):
        return f"""
<div class="tutorial-card">
  <div class="tutorial-number">
    {num}
  </div>
  <div class="tutorial-content">
    <h3 class="tutorial-title">
      {title}
    </h3>
    <div class="tutorial-description">
      <p>{description}</p>
    </div>
    <div class="tutorial-buttons">
      {buttons}
    </div>
  </div>
</div>
"""

    @classmethod
    def _dropdown(cls, step_description, libraries_urls):
        dropdown = f"""
<div id="tutorial-dropdown-{cls._dropdown_id}" class="jq-dropdown jq-dropdown-tip">
    <ul class="jq-dropdown-menu">
"""
        for (library, url) in libraries_urls.items():
            dropdown += f"""
        <li><a href="{url}" target="_blank">{cls._library_image(library)} {library}</a></li>
"""
        dropdown += f"""
    </ul>
</div>
<div class="tutorial-button" data-jq-dropdown="#tutorial-dropdown-{cls._dropdown_id}">{step_description}</div>
"""
        cls._dropdown_id += 1
        return dropdown

    _dropdown_id = 1

    @classmethod
    def _button(cls, step_description, libraries_urls):
        assert len(libraries_urls) == 1
        library = list(libraries_urls.keys())[0]
        url = libraries_urls[library]
        return f"""
    <a href="{url}" target="_blank"><div class="tutorial-button">{cls._library_image(library)} {step_description}</div></a>
"""

    @staticmethod
    def _library_image(library):
        if library == "dolfinx":
            logo = "_static/images/dolfinx-logo.png"
        elif library == "firedrake":
            logo = "_static/images/firedrake-logo.png"
        else:
            raise RuntimeError("Invalid type")
        return f'<img src="{logo}" style="vertical-align: middle; width: 25px">'

def on_build_finished(app, exc):
    if exc is None and app.builder.format == "html":
        # Unescape at symbol
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/%40/@/g' {} +",
            shell=True)
        # Mark current page as active
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + '<li class="md-tabs__item"><a href="#" class="md-tabs__link">'
            + "/"
            + '<li class="md-tabs__item md-tabs__item_current"><a href="#" class="md-tabs__link">'
            + "/g' {} +",
            shell=True)
        # Disable going to submenus on mobile
        subprocess.run(
            "find " + app.outdir + " -type f -not -path '*/\.git/*' -exec sed -i 's/"
            + 'id="__toc"'
            + "/"
            + 'id="__toc_disabled"'
            + "/g' {} +",
            shell=True)
        # Add further SEO tags
        seo_head = """
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "SoftwareApplication",
  "name": "viskex - interactive visualization for firedrake and FEniCSx",
  "description": "viskex is a library for the interactive visualization of finite element simulations within jupyter notebooks in JupyterLab, Google Colab or Kaggle.  viskex is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin.",
  "keywords": "viskex, firedrake, FEniCS, finite element, jupyter, visualization",
  "softwareHelp": "https://viskex.github.io/",
  "operatingSystem": "Linux",
  "applicationCategory": "Simulation",
  "inLanguage": "en",
  "license": "https://opensource.org/licenses/MIT",
  "url": "https://github.com/viskex/viskex"
}
</script>

<meta property="og:title" content="viskex - interactive visualization for firedrake and FEniCSx" />
<meta property="og:description" content="viskex is a library for the interactive visualization of finite element simulations within jupyter notebooks in JupyterLab, Google Colab or Kaggle.  viskex is currently developed at Università Cattolica del Sacro Cuore by Dr. Francesco Ballarin." />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="viskex" />
<meta property="og:url" content="https://viskex.github.io/" />
<meta property="og:image" content="https://viskex.github.io/_images/viskex-logo.png" />
"""
        index = os.path.join(app.outdir, "index.html")
        with open(index, "r") as f:
            index_content = f.read()
        index_content = index_content.replace("<head>", "<head>\n" + seo_head)
        with open(index, "w") as f:
            f.write(index_content)
        # Get tutorial nbconvert html files from git, if not already available
        for num in tutorials.keys():
            for step_files in tutorials[num]["steps"].values():
                for url in step_files.values():
                    if not os.path.exists(os.path.join(app.outdir, url)):
                        html_generated = subprocess.run(
                            "mkdir -p " + os.path.dirname(os.path.join(app.outdir, url)) + " && " +
                            "git show origin/gh-pages:" + url + "> " + os.path.join(app.outdir, url),
                            shell=True, capture_output=True)
                        if html_generated.returncode != 0:
                            raise RuntimeError(
                                "HTML generation of " + url + " not found\n"
                                + "stdout contains " + html_generated.stdout.decode() + "\n"
                                + "stderr contains " + html_generated.stderr.decode() + "\n")


create_sitemap_bak = sphinx_material.create_sitemap
def create_sitemap(app, exc):
    create_sitemap_bak(app, exc)
    if exc is None and app.builder.format == "html":
        # Add version and encoding to the top of sitemap.xml
        subprocess.run(
            "sed -i '1s/^/<?xml version=\"1.0\" encoding=\"UTF-8\"?>/' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
        # Remove trailing index.html from sitemap.xml
        subprocess.run(
            "sed -i 's|/index.html||g' " + os.path.join(app.outdir, "sitemap.xml"),
            shell=True)
sphinx_material.create_sitemap = create_sitemap


def setup(app):
    app.add_directive("tutorials", Tutorials)
    app.connect("build-finished", on_build_finished)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": False,
    }
