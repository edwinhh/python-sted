class FormatFormError:

    @property
    def error_msg(self):
        msg = ''
        for error_key, value in self.errors.get_json_data().items():
            error_message = value[0].get('message')
            m = '%s:%s' % (error_key, error_message)
            msg += m
        return msg
