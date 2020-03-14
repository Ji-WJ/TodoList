from flask_login import login_required, current_user
from flask import abort, render_template, flash, redirect, url_for

from app import db
from app.model import User
from app.user import user
from app.user.forms import EditProfileForm


@user.route('/user/<id>')
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
       abort(404)
    return render_template('user/user.html', user=user)


@user.route('/user/<id>')
def changepasswd(id):
    return 'change passwd'

@user.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('用户配置信息更新成功!', category='success')
        return redirect(url_for('user.get_user', id=current_user.id))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me

    return render_template('user/edit_profile.html', form=form)