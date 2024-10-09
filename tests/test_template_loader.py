import unittest
from unittest.mock import patch

from omni.pro.template.loader import render_to_string


class TestRenderToString(unittest.TestCase):

    @patch("jinja2.Template.render")
    def test_render_to_string(self, mock_render):
        template_name = "Hello, {{ name }}!"
        context = {"name": "World"}

        mock_render.return_value = "Hello, World!"

        result = render_to_string(template_name, context)

        mock_render.assert_called_once_with(context)

        self.assertEqual(result, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
