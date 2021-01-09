#include <QTimer>
#include <QLabel>
#include <QWidget>
#include <QPixmap>
#include <QProgressBar>
#include <QTransform>
#include <QSocketNotifier>

#include <string>
#include <sstream>

#include "common/params.h"

class Spinner : public QWidget {
  Q_OBJECT

public:
  explicit Spinner(QWidget *parent = 0);

private:
  QPixmap track_img;
  QTimer *rotate_timer;
  QLabel *comma, *track;
  QLabel *text;
  QProgressBar *progress_bar;
  QTransform transform;
  QSocketNotifier *notifier;

public slots:
  void rotate();
  void update(int n);
};

int write_param_float(float param, const char* param_name, bool persistent_param = false);
template <class T>
int read_param(T* param, const char *param_name, bool persistent_param = false){
  T param_orig = *param;
  char *value;
  size_t sz;

  int result = Params(persistent_param).read_db_value(param_name, &value, &sz);
  if (result == 0){
    std::string s = std::string(value, sz); // value is not null terminated
    free(value);

    // Parse result
    std::istringstream iss(s);
    iss >> *param;

    // Restore original value if parsing failed
    if (iss.fail()) {
      *param = param_orig;
      result = -1;
    }
  }
  return result;
}
