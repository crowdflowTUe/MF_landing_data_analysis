'''
    File name: MF_domain_related.py
    Author: Alessandro Corbetta
    Date released: 2017-09-27
    Date last modified: 2017-09-27
    Python Version: 2.7
    
    Copyright 2017, Alessandro Corbetta, Crowdflow Research Group, Eindhoven University of Technology
    
    If used please cite
    @article{PhysRevE.95.032316,
      title = {Fluctuations around mean walking behaviors in diluted pedestrian flows},
      author = {Corbetta, Alessandro and Lee, Chung-min and Benzi, Roberto and Muntean, Adrian and Toschi, Federico},
      journal = {Phys. Rev. E},
      volume = {95},
      issue = {3},
      pages = {032316},
      numpages = {9},
      year = {2017}, 
      publisher = {American Physical Society},
      doi = {10.1103/PhysRevE.95.032316},
      url  = {https://link.aps.org/doi/10.1103/PhysRevE.95.032316}
   } 
'''


__author__ = "Alessandro Corbetta"
__copyright__ = "Copyright 2017, Alessandro Corbetta, Crowdflow Research Group, Eindhoven University of Technology"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alessandro Corbetta"
__email__ = "a.corbetta@tue.nl"





## Standard way of plotting Metaforum geometry

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import pandas as pd


par = {}
par = {'X_target' : np.array([8, -.1])
           , 'rcenter' : np.array([.2,-.3])           
           , 'top_wall' : .45
           , 'left_wall' : -2.3
           , 'right_wall' : 2.3
           , 'bot_wall' : -.3
           , 'left_midwall' : -1.3
           , 'right_midwall':  1.3
           , 'max_bottom' : -1.           
           , 'sym_truncation' : 3
           , 'dt' : .1
           , 'obs_left' : -1.1
           , 'obs_right' : 1.1       }

par['right_corner'] = np.array([par['right_midwall'],par['bot_wall']])
par['left_corner'] = np.array([par['left_midwall'],par['bot_wall']])

par['left_target'] = np.array([(par['left_midwall']),par['top_wall']])
par['right_target'] = np.array([.5*(par['right_midwall'] + par['right_wall']),par['max_bottom']-4])

c_center = .175
mid_l = 5.2-1.2-1.2
ext_l = 5.2

par['left_midwall'] = c_center - mid_l/2.  #-1.5 + .2
par['right_midwall'] = c_center + mid_l/2.  #1.5 + .2


par['left_wall'] = c_center - ext_l/2. # -2.5 + .1 -.1
par['right_wall'] = c_center + ext_l/2. #2.5+ .1 +.1

#fixed
par['top_wall'] = .575  #.65
par['bot_wall'] = .575 - 1.2 #-.25 -.1 #-.15

### patch from data
par['obs_right'] = 1.22 # max(tgt_lt0.X.max(),tgt_gt0.X.max())
par['obs_left'] =  -1. #min(tgt_lt0.X.min(),tgt_gt0.X.min())

par['obs_top'] = par['top_wall']  #max(tgt_lt0.Y.max(),tgt_gt0.Y.max())
par['obs_bottom'] = par['obs_left'] # -.61 # min(tgt_lt0.Y.min(),tgt_gt0.Y.min())


def draw_boundaries(par,color = 'b'
                    , true_mirroring = False
                    , stairs = True
                    , side_boxes = True
                    , color_main_block = 'k' ):
    if true_mirroring:
        sgn = -1.
    else:
        sgn = 1.

    


    plt.plot([sgn * par['left_wall'],sgn *  par['right_wall']],[par['top_wall'],par['top_wall']],color)    
    plt.plot([sgn * par['left_midwall'], sgn * par['right_midwall']],[par['bot_wall'],par['bot_wall']],color)
    plt.plot([sgn * par['left_wall'],sgn * par['left_wall']],[par['top_wall'],par['max_bottom']],color)
    plt.plot([sgn * par['right_wall'],sgn * par['right_wall']],[par['top_wall'],par['max_bottom']],color)
    plt.plot([sgn * par['left_midwall'],sgn * par['left_midwall']],[par['bot_wall'],par['max_bottom']],color)
    plt.plot([sgn * par['right_midwall'],sgn * par['right_midwall']],[par['bot_wall'],par['max_bottom']],color)

    #plt.plot([par['obs_right'],par['obs_right']],[par['bot_wall'],par['top_wall']],color)
    #plt.plot([par['obs_left'],par['obs_left']],[par['bot_wall'],par['top_wall']],color)
    
    
    plt.plot([sgn * par['obs_left'],sgn * par['obs_right']],[par['bot_wall'],par['bot_wall']],color_main_block)
    plt.plot([sgn * par['obs_left'],sgn * par['obs_right']],[par['top_wall'],par['top_wall']],color_main_block)
    #plt.plot([1.,1.],[par['bot_wall'],par['top_wall']],'.5')
    plt.plot([sgn * par['obs_left'],sgn * par['obs_left']],[par['bot_wall'],par['top_wall']],color_main_block)
    plt.plot([sgn * par['obs_right'],sgn * par['obs_right']],[par['bot_wall'],par['top_wall']],color_main_block)
    
    

    small_dom_left = sgn* ( -.8)
    small_dom_right = sgn* ( 1.)


    if side_boxes:

        plt.plot([small_dom_left,small_dom_right],[par['bot_wall'],par['bot_wall']],'.5')
        plt.plot([small_dom_left,small_dom_right],[par['top_wall'],par['top_wall']],'.5')
        #plt.plot([1.,1.],[par['bot_wall'],par['top_wall']],'.5')
        plt.plot([small_dom_left,small_dom_left],[par['bot_wall'],par['top_wall']],'.5',alpha=.9)
        plt.plot([small_dom_right,small_dom_right],[par['bot_wall'],par['top_wall']],'.5',alpha=.9)


    if true_mirroring and stairs:
        stair_size = .25
        plt.plot([sgn * par['left_wall'], sgn * par['left_midwall']] ,[par['bot_wall'] , par['bot_wall']],color)
        plt.plot([sgn * par['left_wall'], sgn * par['left_midwall']] ,[par['bot_wall'] - stair_size , par['bot_wall'] - stair_size],color)

        
        plt.plot([sgn * par['right_wall'], sgn * par['right_midwall']] ,[par['bot_wall'] , par['bot_wall']],color)
        plt.plot([sgn * par['right_wall'], sgn * par['right_midwall']] ,[par['bot_wall'] - stair_size , par['bot_wall'] - stair_size],color)


    
    if side_boxes:

        if not true_mirroring:
            currentAxis = plt.gca()
            currentAxis.add_patch(Rectangle((small_dom_left, par['bot_wall']), par['obs_left'] + .8 ,  1.2, facecolor=".9",alpha = .5))
            currentAxis.add_patch(Rectangle((small_dom_right , par['bot_wall']), par['obs_right'] - 1. ,  1.2, facecolor=".9",alpha = .5))
        else:
            currentAxis = plt.gca()
            currentAxis.add_patch(Rectangle((small_dom_left, par['bot_wall']), -(par['obs_left'] + .8) ,  1.2, facecolor=".9",alpha = .5))
            currentAxis.add_patch(Rectangle((small_dom_right , par['bot_wall']), -(par['obs_right'] - 1.) ,  1.2, facecolor=".9",alpha = .5))

    
def draw_domain_std(seaborn_import = False
                    , true_mirroring = False
                    , stairs = False
                    , **kw):
    if seaborn_import:
        import seaborn as sns
        sns.set_style("whitegrid")

    draw_boundaries(par,'k--',true_mirroring = true_mirroring, stairs = stairs,**kw)

def draw_domain_axis(pstyle,true_mirroring = False,**kw):
    mid_x = .5 * (par['left_midwall'] + par['right_midwall'])
    if true_mirroring:
        plt.plot([- mid_x, - mid_x],[par['bot_wall'],par['top_wall']],pstyle,**kw)
    else:
        print "WARNING: not implemented for true_mirroring == False"

    
def draw_domain_std_close(true_mirroring = False
                          , just_domain = False
                          , sharp_boundary = False
                          , xlabel = '$x\,$[m]' 
                          , ylabel = '$y\,$[m]'
                          , xticks = None
                          , yticks = None
                          , xticks_kw = {}
                          , yticks_kw = {}
                          , xlabel_kw = {}
                          , ylabel_kw = {}):
    plt.axis('scaled')
    if true_mirroring:
        if xticks is None:
            plt.xticks([-3.,-2.,-1,0.,1.,2.],**xticks_kw)
        else:
            plt.xticks(xticks,**xticks_kw)


        if just_domain:
            plt.xlim([- (par['right_midwall'] -.25),-(par['left_midwall'] + .15 )])
            plt.ylim([par['max_bottom'] +.25 ,par['top_wall'] +.1])
        else:
            plt.xlim([- (par['right_wall'] +.2),-(par['left_wall'] - .2)])
            plt.ylim([par['max_bottom'] ,par['top_wall'] +.1])

        if sharp_boundary:
            plt.xlim([- (par['right_midwall'] -.525),-(par['left_midwall'] + .425 )])
            plt.ylim([par['max_bottom'] +.325 ,par['top_wall'] +.05])

        if not sharp_boundary and not just_domain:
            if yticks is None:
                plt.yticks([-1.,-.6,-.2,.2,.6],**yticks_kw)
            else:
                plt.yticks(yticks,**yticks_kw)

        
    else:
        if just_domain:
            print "WARNING: just_domain = True in combination with true_mirroring = False has to be implemented"

        

        if xticks is None:
            #plt.xticks([-3.,-2.,-1,0.,1.,2.])
            plt.xticks([-2.5,-2.,-1.5,-1,-.5,0.,.5,1.,1.5,2.,2.5,3.])
        else:
            plt.xticks(xticks)


        plt.xlim([par['left_wall'] - .2,par['right_wall'] +.2])
        plt.ylim([par['max_bottom'] ,par['top_wall'] +.1])


    plt.xlabel(xlabel,**xlabel_kw)
    plt.ylabel(ylabel,**ylabel_kw)


def plot_pref_post_layer(df_i
                         , sty
                         , do_plot = True
                         , bins = np.linspace(-.8,1.,20)
                         , beg_mask = None
                         , end_mask = None
                         , label = ''
                         , alpha = .5
                         , plot_band_between = False
                         , fill_betw_kw = {}
                         , **kw):
    groups = pd.cut(df_i.X,bins)
    df = df_i.groupby(groups)


    any_plotting = any([do_plot
                        , plot_band_between])

    if any_plotting:
        X_val = -df.X.mean()[beg_mask:end_mask]
        Y_val_bottom = df.Y.quantile(.15)[beg_mask:end_mask]
        Y_val_top = df.Y.quantile(.85)[beg_mask:end_mask] 

    if do_plot:
        plt.plot(X_val
                 , Y_val_bottom
                 , sty,alpha=alpha,label=label
                 , **kw)
        plt.plot(X_val
                 , Y_val_top
                 , sty,alpha=alpha,label=''
                 , **kw)

    if plot_band_between:
        plt.fill_between(
            X_val
            , Y_val_bottom
            , Y_val_top
            , ** fill_betw_kw
        )

    

    return {
        'x_coord' : -df.X.mean()[beg_mask:end_mask]
        , 'top_line' : df.Y.quantile(.15)[beg_mask:end_mask]
        , 'bottom_line' : df.Y.quantile(.85)[beg_mask:end_mask]
    }


def quiver_compare_lines(baseline,to_diff,arg):
    ou_la = baseline
    ou_eu = to_diff
    plt.quiver(ou_la['x_coord']
               , ou_la[arg]
               , np.zeros([len(ou_la[arg])])
               , ou_eu[arg] - ou_la[arg]               
               , scale_units='xy'
               #, angles='xy'
               , scale=1)


bins_x_std = np.linspace(-.8 , 1. , 32)
bins_y_std = np.linspace(-1. , .5 , 20)

mid_pts = lambda x : .5 * (x[1:] + x[:-1])

def cut_data(data
             , outfields = ['Speed_SG']
             , subquery = None
             , Xf = 'X_SG' 
             , Yf = 'Y_SG'
             , bins_x = bins_x_std
             , bins_y = bins_y_std
             ):
    
    cuts_x = pd.cut(data[Xf], bins_x,labels=False)
    cuts_y = pd.cut(data[Yf], bins_y,labels=False)
    
    if subquery is not None:
        target_data = data.query(subquery)
    else:
        target_data = data
          
    return target_data[[Xf,Yf] + outfields].groupby([cuts_x,cuts_y])


def cut_data_get_reindex_for_spatial_plot(bins_x = bins_x_std
                                          , bins_y = bins_y_std
                                      ):
    return [(x,y) for x in range(len(bins_x)-1) for y in range(len(bins_y)-1)]



def generate_spatial_field_from_groups(grps,getter,reindex__):
    # grp_sgt0.Speed_SG.mean().reindex(reindex__).unstack().transpose()
    return getter(grps).mean().reindex(reindex__).unstack().transpose()

    


def full_contour_plot_lambda(data
                             , getter
                             , vlevs
                             , plotting_f = plt.contourf
                             , bins_x = bins_x_std
                             , bins_y = bins_y_std
                             , x_multiplier = -1.
                             , do_plot = True
                             , outfields = ['Speed_SG']
                             , **kw
                         ):

    cut_data_grps = cut_data(data
                             , outfields = outfields
                             , bins_x = bins_x
                             , bins_y = bins_y)

    reindex__= cut_data_get_reindex_for_spatial_plot(bins_x = bins_x
                                                     , bins_y = bins_y)

    
    spatial_field = generate_spatial_field_from_groups( cut_data_grps 
                                                        , getter 
                                                        , reindex__ )

    ret = {
        'cut_data_grps' : cut_data_grps
        , 'reindex__' : reindex__
        , 'spatial_field' : spatial_field
    }

    if do_plot:
        
        CPlt = plotting_f(x_multiplier * mid_pts(bins_x)
                          , mid_pts(bins_y)
                          , spatial_field #speed_sgt0_v
                          , vlevs
                          , **kw)

        ret['CPlt'] = CPlt

    return ret

def full_contour_plot_lambda_compare( data1
                                      , data2
                                      , getter
                                      , vlevs
                                      , plotting_f = plt.contourf
                                      , bins_x = bins_x_std
                                      , bins_y = bins_y_std
                                      , x_multiplier = -1.
                                      , **kw
                                  ):
    
    o1 = full_contour_plot_lambda(
        data1
        , getter
        , vlevs
        , plotting_f = plt.contourf
        , bins_x = bins_x_std
        , bins_y = bins_y_std
        , x_multiplier = -1.
        , do_plot = False
            )

    o2 = full_contour_plot_lambda(
        data2
        , getter
        , vlevs
        , plotting_f = plt.contourf
        , bins_x = bins_x_std
        , bins_y = bins_y_std
        , x_multiplier = -1.
        , do_plot = False
            )


    CPlt = plotting_f(x_multiplier * mid_pts(bins_x)
                      , mid_pts(bins_y)
                      , o1['spatial_field'] - o2['spatial_field']
                      , vlevs
                      , **kw)

    return {
        'o1' : o1
        , 'o2' : o2
        , 'CPlt' : CPlt
    }


   


def contours_plus_contourf_plus_text(  m_bins_x
                                       , m_bins_y
                                       , field
                                       , vlevs 
                                       , **kw):


    try:
        kw_args_contourf = kw['kw_args_contourf']

    except:
        kw_args_contourf = {}

    CPlt = plt.contourf(
        m_bins_x
        , m_bins_y
        , field
        , vlevs
        , **kw_args_contourf )


    CS2 = plt.contour(CPlt, levels=CPlt.levels[0::1],
                      linewidths = .4,
                      colors='w',                  
                      hold='on')

    plt.clabel(CS2, CPlt.levels[1::2],  # label every second level
               inline=1,
               fmt='%1.1f',
               fontsize=10)

    return CPlt

annotate_direction_2L = lambda  size='large',append_note='',prepend_note='' : plt.annotate('\%s{%s2L ($\\leftarrow$)%s}'%(size,prepend_note,append_note) , xy=(0,-0.55),bbox=dict(boxstyle='round', fc='white', alpha=0.9)) 

annotate_direction_2R = lambda  size='large',append_note='',prepend_note='' : plt.annotate('\%s{%s2R ($\\rightarrow$)%s}'%(size,prepend_note,append_note) , xy=(0,-0.55),bbox=dict(boxstyle='round', fc='white', alpha=0.9)) 

class Domain_plotter_cm():
    def __init__(self
                 , sharp_boundary = False
                 , annotate_direction = ''
                 , just_domain = True
                 , xticks = None
                 , yticks = None
                 , annotate_direction_size = None
                 , annotate_direction_append_note = ''
                 , annotate_direction_prepend_note = ''
                 , **kw):
        self.stairs = True
        self.true_mirroring = True
        self.just_domain = just_domain
        self.sharp_boundary = sharp_boundary
        self.annotate_direction = annotate_direction
        self.xticks = xticks
        self.yticks = yticks
        self.annotate_direction_size = annotate_direction_size
        self.annotate_direction_append_note = annotate_direction_append_note
        self.annotate_direction_prepend_note = annotate_direction_prepend_note
        self.kw = kw

    def __enter__(self):
        draw_domain_std(true_mirroring = self.true_mirroring,stairs=self.stairs,**self.kw)


    def __exit__(self, type, value, traceback):
        draw_domain_axis(':',true_mirroring = self.true_mirroring,color='grey')

        if self.annotate_direction == '2L':
            ann_dir_fcall = annotate_direction_2L
        elif self.annotate_direction == '2R':
            ann_dir_fcall = annotate_direction_2R
        else:
            ann_dir_fcall = lambda *args,**kw : None

        if self.annotate_direction_size is not None:
            ann_dir_fcall(size = self.annotate_direction_size
                          , append_note = self.annotate_direction_append_note
                          , prepend_note = self.annotate_direction_prepend_note)
        else:
            ann_dir_fcall(append_note = self.annotate_direction_append_note
                          , prepend_note = self.annotate_direction_prepend_note )

        draw_domain_std_close(true_mirroring = self.true_mirroring
                              , just_domain = self.just_domain
                              , sharp_boundary = self.sharp_boundary
                              , xticks = self.xticks
                              , yticks = self.yticks)


def plot_selected_trajs(df,pid_list):

    with Domain_plotter_cm(side_boxes = False
                           , just_domain = False
                            , sharp_boundary = False
                           , annotate_direction = ''
                           , color_main_block = '.8'):
        
        for pid_ in pid_list:
            df.query('Pid == @pid_').groupby('Pid').apply(lambda x : plt.plot(-x.X_SG , x.Y_SG))  
