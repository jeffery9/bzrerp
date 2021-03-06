# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from datetime import datetime

class bzr_hr_employee_type(osv.osv):
    """
        员工类型 bzr.hr.employee.type
        管理人员
        业务人员
        计时员工
        计件员工
    """
    _name='bzr.hr.employee.type'
    _description=u'员工类型'
    _columns={
        'name':fields.char(u'类型',size=50,required=True),
    }

class bzr_hr_department_type(osv.osv):
    """
        部门 bzr.hr.department.type
        管理部门
        业务部门
    """
    _name='bzr.hr.department.type'
    _description=u'部门类型'
    _columns={
        'name':fields.char(u'类型',size=50,required=True),
    }

