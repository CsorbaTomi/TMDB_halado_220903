import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Item{
    ColumnLayout{
        anchors.fill: parent
        anchors.leftMargin: 5
        spacing: 20

        // Search by title
        IconTextField{id: search_by_title; placeholder_text: "Search by title"; icon: Resources.get("search.svg")}

        // Sorting
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: 100

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                SubtitleText{
                    text: "Sort result by:"
                }

                ComboBox{
                    model: [
                        "Popularity Descending", 
                        "Popularity Ascending",
                        "Rating Descending",
                        "Rating Ascending",
                        "Release Date Descending",
                        "Release Date Ascending",
                        "Title (A-Z)",
                        "Title (Z-A)"
                    ]
                    Layout.fillWidth: true

                    onActivated: print("Sort by:", currentText, currentIndex)
                }
            }
        }

        // Genre filter
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: 100

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                SubtitleText{
                    text: "Genres"
                }
            }
        }

        // spacer
        Item{
            Layout.fillHeight: true
        }
    }
}