from edit_service import EditService

class RecordService():

    # Script header (imports etc.) will be set up in Main when record is clicked.
    def __init__(self, script, edit_service, connection_string, record=False):
        self._script = script
        self._edit_service = edit_service
        self._connection_string = connection_string
        self._record = record

    ###################
    # Filters
    ###################
    def filter_value(self, value, operator):
        self._edit_service.filter_value(value, operator)
        if self._record:
            self._script("edit_service.filter_value(%s, '%s')\n" % (value, operator), 'black')

    def filter_date(self, before, after):
        self._edit_service.filter_date(before, after)
        if self._record:
            self._script("edit_service.filter_date(%s, %s)\n" % (repr(before), repr(after)), 'black')

    def data_gaps(self, value, time_period):
        self._edit_service.data_gaps(value, time_period)
        if self._record:
            self._script("edit_service.data_gaps(%s, '%s')\n" % (value, time_period), 'black')

    def value_change_threshold(self, value):
        self._edit_service.value_change_threshold(value)
        if self._record:
            self._script("edit_service.value_change_threshold(%s)\n" % (value), 'black')

    def toggle_filter_previous(self):
        self._edit_service.toggle_filter_previous()

    def select_points_tf(self, tf_list):
        self._edit_service.select_points_tf(tf_list)
        if self._record:
            self._script("#Lasso selection")        # TODO: write dv datetimes to script

    def select_points(self, id_list=[], datetime_list=[]):
        self._edit_service.select_points(id_list, datetime_list)
        if self._record:
            self._script("#Lasso selection")


    ###################
    # Editing
    ###################
    def add_points(self, points):
        self._edit_service.add_points(points)
        if self._record:
            self._script("# add points")

    def delete_points(self):
        self._edit_service.delete_points()
        if self._record:
            self._script("edit_service.delete_points()\n", 'black')

    def change_value(self, operator, value):
        self._edit_service.change_value(operator, value)
        if self._record:
            self._script("edit_service.change_value(%s, '%s')\n" % (operator, value), 'black')

    def interpolate(self):
        self._edit_service.interpolate()
        if self._record:
            self._script("edit_service.interpolate()", 'black')

    def drift_correction(self, gap_width):
        ret = self._edit_service.drift_correction(gap_width)
        if self._record:
            self._script("edit_service.drift_correction(%s)" % (gap_width), 'black')

        return ret

    def reset_filter(self):
        self._edit_service.reset_filter()
        if self._record:
            self._script("edit_service.reset_filter()\n", 'black')

    def flag(self, qualifier_id):
        self._edit_service.flag(qualifier_id)
        if self._record:
            self._script("edit_service.flag(%s)\n" % qualifier_id, 'black')

    def restore(self):
        self._edit_service.restore()
        if self._record:
            self._script("edit_service.restore()\n", 'black')

    def save(self):
        self._edit_service.save()
        if self._record:
            self._script("edit_service.save()\n", 'black')

    ###################
    # Gets
    ###################
    def get_series(self):
        return self._edit_service.get_series()

    def get_series_points(self):
        return self._edit_service.get_series_points()

    def get_filtered_points(self):
        return self._edit_service.get_filtered_points()

    def get_filter_list(self):
        return self._edit_service.get_filter_list()

    def get_selection_groups(self):
        return self._edit_service.get_selection_groups()

    def toggle_record(self):
        if self._record:
            self._record = False
        else:
            self._record = True

    ###################
    # Creates
    ###################
    def create_qcl(self, code, definition, explanation):
        qcl = self._edit_service.create_qcl(code, definition, explanation)
        if self._record:
            self._script('new_qcl = series_service.get_qcl_by_id(%s)\n' % (qcl.id))

    def write_header(self):
        self._script("from odmservices import EditService\n", 'black')
        self._script("from odmservices import SeriesService\n", 'black')
        self._script("edit_service   = EditService(series_id=%s, connection_string='%s')\n" % (self._edit_service._series_id, self._connection_string), 'black')
        self._script("series_service = SeriesService(connection_string='%s')\n" % (self._connection_string), 'black')