import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "custom_widgets"

Item{
    ColumnLayout{
        anchors.fill: parent
        anchors.leftMargin: 5

        // Search by title
        IconTextField{id: search_by_title; placeholder_text: "Search by title"; icon: Resources.get("search.svg")}

        // Sorting
        CustomRectangle{
            Layout.fillWidth: true
            implicitHeight: 100

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                Text{
                    text: "Sort result by:"
                    font.bold: true
                    font.pixelSize: 16
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
                }
            }
        }

        // spacer
        Item{
            Layout.fillHeight: true
        }
    }
}