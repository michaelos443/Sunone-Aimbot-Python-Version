"""
Script to create a Notion page for the Seaborn Export Module documentation.

To use this script:
1. Install the Notion SDK: pip install notion-client
2. Set your Notion API key as an environment variable: NOTION_API_KEY
3. Set your parent page or database ID as an environment variable: NOTION_PARENT_ID
4. Run this script: python create_notion_page.py
"""

import os
import json
from notion_client import Client

# Initialize the Notion client
notion = Client(auth=os.environ.get("NOTION_API_KEY"))

# Parent page or database ID
parent_id = os.environ.get("NOTION_PARENT_ID")

# Check if we're adding to a database or a page
is_database = True  # Set to False if adding to a page instead of a database

# Create the page content
if is_database:
    # Create a page in a database
    new_page = {
        "parent": {"database_id": parent_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "Seaborn Export Module Documentation"
                        }
                    }
                ]
            },
            # Add other properties as needed for your database
        },
        "children": [
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": "📊 Seaborn Export Module"}}]
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Overview"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "A new export module has been added to the seaborn library that allows users to easily save figures in multiple file formats with a single function call. This module simplifies the process of exporting visualizations for publications, presentations, or web content."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Key Features"}}]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "💾 Multi-format export - Save figures in various formats (PNG, PDF, SVG, JPEG, TIFF, etc.)"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🏷️ Legend extraction - Extract and save just the legend from a plot as a separate file"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🔍 High-resolution support - Control resolution (DPI) for high-quality exports"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🔄 Batch processing - Save in multiple formats with one command"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🖼️ Transparency control - Save with transparent backgrounds for better integration"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Implementation Details"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "The module consists of the following components:"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "caption": [],
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "seaborn/export.py         # Main module file containing export functionality\nseaborn/__init__.py       # Updated to include the new module\nexamples/export_example.py # Comprehensive examples demonstrating usage\ntests/test_export.py      # Unit tests ensuring functionality works correctly"
                            }
                        }
                    ],
                    "language": "plain text"
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Code Examples"}}]
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": "Basic Usage"}}]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "caption": [],
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "import seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Create a simple plot\ntips = sns.load_dataset(\"tips\")\nsns.scatterplot(data=tips, x=\"total_bill\", y=\"tip\")\n\n# Save in multiple formats\nsns.save_figure(formats=[\"png\", \"pdf\", \"svg\"])"
                            }
                        }
                    ],
                    "language": "python"
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": "Advanced Usage"}}]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "caption": [],
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "import seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Create a plot with a legend\ntips = sns.load_dataset(\"tips\")\nsns.scatterplot(data=tips, x=\"total_bill\", y=\"tip\", hue=\"time\")\n\n# Get the legend\nlegend = plt.gca().get_legend()\n\n# Export the main figure with high resolution\nsns.save_figure(\n    path=\"figures/tips_scatter\",\n    formats=[\"png\", \"jpg\"],\n    dpi=300\n)\n\n# Export just the legend\nsns.export_legend(\n    legend,\n    path=\"figures/tips_legend\",\n    formats=[\"png\", \"pdf\"]\n)"
                            }
                        }
                    ],
                    "language": "python"
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "API Reference"}}]
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": "save_figure()"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Save a matplotlib figure in one or multiple file formats."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "caption": [],
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "save_figure(\n    fig=None,\n    path=\"seaborn_plot\",\n    formats=\"png\",\n    dpi=300,\n    quality=None,\n    transparent=False,\n    bbox_inches=\"tight\",\n    pad_inches=0.1,\n    facecolor=None,\n    **kwargs\n)"
                            }
                        }
                    ],
                    "language": "python"
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Parameters:"
                            },
                            "annotations": {
                                "bold": true
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "fig: The figure to save. If None, uses the current figure."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "path: The path where the figure should be saved, without file extension."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "formats: The file format(s) to save the figure in. Can be a single format or a list of formats."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "dpi: The resolution in dots per inch."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "quality: For JPEG format only, the image quality from 1 to 100."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "transparent: If True, the figure background will be transparent (for formats that support transparency)."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": "export_legend()"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Export only the legend of a plot to a separate file."
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "caption": [],
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "export_legend(\n    legend,\n    path=\"legend\",\n    formats=\"png\",\n    **kwargs\n)"
                            }
                        }
                    ],
                    "language": "python"
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Status and Links"}}]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "✅ Pull request created and merged"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "✅ All tests passing"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "📝 Documentation available on:"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Confluence",
                                "link": {
                                    "url": "https://test-team-e43poqe8.atlassian.net/wiki/spaces/SD/pages/9961473/Seaborn+Export+Module+Documentation"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Linear Issue TES-20",
                                "link": {
                                    "url": "https://linear.app/test-workspace-aug/issue/TES-20/seaborn-export-module-documentation"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "GitHub Pull Request #1",
                                "link": {
                                    "url": "https://github.com/michaelos443/seaborn/pull/1"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
else:
    # Create a page as a child of another page
    new_page = {
        "parent": {"page_id": parent_id},
        "properties": {
            "title": [
                {
                    "text": {
                        "content": "Seaborn Export Module Documentation"
                    }
                }
            ]
        },
        # Add the same children blocks as above
    }

try:
    # Create the page
    response = notion.pages.create(**new_page)
    print(f"Successfully created Notion page: {json.dumps(response, indent=2)}")
    print(f"Page URL: {response['url']}")
except Exception as e:
    print(f"Error creating Notion page: {e}")
